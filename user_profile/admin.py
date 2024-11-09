from django.contrib import admin
from .models import UserProfile, Monster, UserMonster

# 註冊用戶資料
admin.site.register(UserProfile)

# 註冊怪獸資料
admin.site.register(Monster)

# 註冊用戶與怪獸關係
admin.site.register(UserMonster)