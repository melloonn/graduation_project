from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserProfile, Monster
from login.models import User

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        獲取用戶的 Profile 資訊，包括 Gems、Coins、Nickname、Photo 和擁有的 Monsters。
        """
        user = request.user  # 從 Token 解碼後獲取的 User
        try:
            profile = UserProfile.objects.get(user=user)
            monsters = Monster.objects.filter(user_profile=profile)

            response_data = {
                "userID": user.username,
                "nickname": profile.nickname,
                "gems": profile.gems,
                "coins": profile.coins,
                "photo": profile.photo,
                "monsters": [monster.monster_name for monster in monsters],
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        更新 Profile 資訊或新增怪獸到用戶的 Monster 表。
        """
        user = request.user
        data = request.data

        try:
            profile, created = UserProfile.objects.get_or_create(user=user)

            # 更新 Profile 資訊
            profile.nickname = data.get("nickname", profile.nickname)
            profile.gems = data.get("gems", profile.gems)
            profile.coins = data.get("coins", profile.coins)
            profile.photo = data.get("photo", profile.photo)
            profile.save()

            # 新增怪獸（如果提供了怪獸名稱）
            new_monster = data.get("new_monster")
            if new_monster:
                # 檢查怪獸是否已存在
                if not Monster.objects.filter(user_profile=profile, monster_name=new_monster).exists():
                    Monster.objects.create(user_profile=profile, monster_name=new_monster)

            return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)