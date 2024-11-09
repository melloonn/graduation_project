from django.db import models
from login.models import User  # 從 login app 引入 User 模型

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="profile")
    nickname = models.CharField(max_length=50, blank=True, null=True)  # 用戶暱稱
    gems = models.IntegerField(default=0)  # 遊戲的 Gems
    coins = models.IntegerField(default=0)  # 遊戲的金幣
    photo = models.IntegerField(default=0)  # 大頭貼 (使用 monster 的代號)

    def __str__(self):
        return f"{self.user.username} - Profile"

class Monster(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="monsters")
    monster_name = models.CharField(max_length=50)  # 怪獸名稱，例如 monster1, monster2, ...
    
    def __str__(self):
        return f"{self.user_profile.user.username} owns {self.monster_name}"