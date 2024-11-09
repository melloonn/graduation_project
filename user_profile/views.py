from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserProfile, UserMonster, Monster 


class UserProfileAPIView(APIView):
    """
    用戶資料 API：
    - GET: 根據用戶的 Token 獲取用戶的所有數據（包括金幣、寶石、分數和怪獸）。
    - POST: 更新用戶的資料（金幣、寶石、分數和怪獸）。
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        try:
            profile = UserProfile.objects.get(user=user)
            
            # 獲取用戶的所有怪獸，如果沒有則返回空清單
            user_monsters = UserMonster.objects.filter(user_profile=profile)
            monsters = [
                {"monster_id": monster.monster.monster_id, "monster_name": monster.monster.monster_name}
                for monster in user_monsters
            ]

            response_data = {
                "userID": user.username,
                "nickname": profile.nickname,
                "coins": profile.coins,
                "gems": profile.gems,
                "score": profile.score,
                "monsters": monsters,  # 如果沒有怪獸，將返回空清單
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user = request.user
        data = request.data
        try:
            # 獲取或創建用戶的 UserProfile
            profile, _ = UserProfile.objects.get_or_create(user=user)

            # 更新用戶資料
            profile.coins = data.get("coins", profile.coins)
            profile.gems = data.get("gems", profile.gems)
            profile.score = data.get("score", profile.score)

            # 更新 nickname
            profile.nickname = data.get("nickname", profile.nickname)

            # 保存更改
            profile.save()

            # 返回成功消息
            return Response({"message": "用戶資料更新成功"}, status=status.HTTP_200_OK)

        except Exception as e:
            # 處理可能的異常
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LeaderboardAPIView(APIView):
    """
    排行榜 API:
    - 獲取分數前 10 名的用戶資料，按分數降序排序。
    """
    def get(self, request):
        try:
            # 獲取前 10 名分數最高的用戶資料
            top_profiles = UserProfile.objects.order_by('-score')[:10]
            leaderboard = [
                {
                    "name": profile.nickname if profile.nickname else profile.user.username,  # 判斷使用 nickname 或 username
                    "score": profile.score,
                }
                for profile in top_profiles
            ]
            return Response(leaderboard, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)