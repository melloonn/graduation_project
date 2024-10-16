from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class AuthTests(APITestCase):

    def setUp(self):
        # 創建一個測試用戶
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')
        self.token_refresh_url = reverse('token_refresh')

    def test_register(self):
        """
        測試註冊功能
        """
        data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'email': 'newuser@example.com'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')
        self.assertEqual(response.data['email'], 'newuser@example.com')
    
    def test_login(self):
        """
        測試登錄功能
        """
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
    
    def test_login_invalid_credentials(self):
        """
        測試無效憑證的登錄
        """
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

    def test_token_refresh(self):
        """
        測試刷新 JWT token
        """
        # 首先進行登錄來獲取 refresh token
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        login_response = self.client.post(self.login_url, data)
        refresh_token = login_response.data['refresh']

        # 使用刷新 token 來獲取新的 access token
        refresh_data = {
            'refresh': refresh_token
        }
        response = self.client.post(self.token_refresh_url, refresh_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_logout(self):
        """
        測試登出功能
        """
        # 先進行登錄，獲取 token
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        login_response = self.client.post(self.login_url, data)
        access_token = login_response.data['access']

        # 使用 token 進行登出
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
