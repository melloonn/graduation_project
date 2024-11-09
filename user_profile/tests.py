from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from user_profile.models import UserProfile, Monster, UserMonster
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()


class UserProfileAPITest(TestCase):
    def setUp(self):
        """
        初始化測試數據
        """
        # 創建用戶
        self.user1 = User.objects.create_user(username='user1', password='password1', email='user1@example.com')
        self.user2 = User.objects.create_user(username='user2', password='password2', email='user2@example.com')
        self.user3 = User.objects.create_user(username='user3', password='password3', email='user3@example.com')

        # 創建怪獸
        self.monster1 = Monster.objects.create(monster_id=1, monster_name="monster1")
        self.monster2 = Monster.objects.create(monster_id=2, monster_name="monster2")
        self.monster3 = Monster.objects.create(monster_id=3, monster_name="monster3")

        # 創建用戶資料和關聯怪獸
        UserProfile.objects.create(user=self.user1, coins=100, gems=50, score=200, photo=1)
        UserProfile.objects.create(user=self.user2, coins=200, gems=75, score=300, photo=2)
        UserProfile.objects.create(user=self.user3, coins=150, gems=60, score=100, photo=3)

        UserMonster.objects.create(user_profile=self.user1.userprofile, monster=self.monster1)
        UserMonster.objects.create(user_profile=self.user2.userprofile, monster=self.monster2)
        UserMonster.objects.create(user_profile=self.user3.userprofile, monster=self.monster3)

        # 初始化 API 客戶端
        self.client = APIClient()

        # 獲取用戶的 Token
        response = self.client.post('/login/login/', {'username': 'user1', 'password': 'password1'}, format='json')
        self.access_token_user1 = response.data['access']

        response = self.client.post('/login/login/', {'username': 'user2', 'password': 'password2'}, format='json')
        self.access_token_user2 = response.data['access']

    def test_get_user_profile(self):
        """
        測試獲取用戶資料
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token_user1}')
        response = self.client.get('/user_profile/profile/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['userID'], 'user1')
        self.assertEqual(response.data['coins'], 100)
        self.assertEqual(response.data['gems'], 50)
        self.assertEqual(response.data['score'], 200)
        self.assertEqual(response.data['photo'], 1)
        self.assertEqual(response.data['monsters'], ['monster1'])

    def test_update_user_profile(self):
        """
        測試更新用戶資料
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token_user1}')
        update_data = {
            "coins": 500,
            "gems": 100,
            "score": 400,
            "photo": 2
        }
        response = self.client.post('/user_profile/profile/', update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "用戶資料更新成功")

        # 驗證數據是否更新
        profile = UserProfile.objects.get(user=self.user1)
        self.assertEqual(profile.coins, 500)
        self.assertEqual(profile.gems, 100)
        self.assertEqual(profile.score, 400)
        self.assertEqual(profile.photo, 2)

    def test_get_leaderboard(self):
        """
        測試獲取排行榜
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token_user1}')
        response = self.client.get('/user_profile/leaderboard/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # 有 3 個用戶

        # 驗證排名
        self.assertEqual(response.data[0]['userID'], 'user2')  # 分數最高
        self.assertEqual(response.data[1]['userID'], 'user1')  # 第二高
        self.assertEqual(response.data[2]['userID'], 'user3')  # 第三高

    def test_unauthorized_access(self):
        """
        測試未經授權的訪問
        """
        response = self.client.get('/user_profile/profile/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post('/user_profile/profile/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get('/user_profile/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)