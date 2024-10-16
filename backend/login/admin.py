from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 註冊自定義的 User 模型
admin.site.register(User, UserAdmin)