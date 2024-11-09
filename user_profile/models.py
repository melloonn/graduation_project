from django.db import models
from django.conf import settings  # 引入 settings


class UserProfile(models.Model):
    """
    用戶資料表：
    - user: 關聯到自定義的用戶模型
    - nickname: 用戶的暱稱
    - coins: 用戶的金幣
    - gems: 用戶的寶石數量
    - photo: 用戶的大頭貼，對應怪獸的代號
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=50, blank=True, null=True, help_text="用戶的暱稱")
    coins = models.IntegerField(default=0, help_text="用戶的金幣")
    gems = models.IntegerField(default=0, help_text="用戶的寶石數量")
    photo = models.IntegerField(blank=True, null=True, help_text="用戶大頭貼的怪獸代號")
    score = models.IntegerField(default=0, help_text="用戶的分數")

    def __str__(self):
        return f"{self.user.username} - Profile"


class Monster(models.Model):
    """
    怪獸表：
    - monster_id: 怪獸的唯一代號
    - monster_name: 怪獸名稱
    """
    monster_id = models.IntegerField(primary_key=True, help_text="怪獸的唯一代號")
    monster_name = models.CharField(max_length=50, help_text="怪獸名稱")

    def __str__(self):
        return f"Monster {self.monster_id} - {self.monster_name}"


class UserMonster(models.Model):
    """
    用戶怪獸表：
    - user_profile: 關聯到用戶的資料表
    - monster: 關聯到怪獸表
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_monsters")
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name="user_owners")

    def __str__(self):
        return f"{self.user_profile.user.username} owns {self.monster.monster_name}"