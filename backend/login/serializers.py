from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']  # 僅包括模型中存在的字段
        extra_kwargs = {'password': {'write_only': True}}


