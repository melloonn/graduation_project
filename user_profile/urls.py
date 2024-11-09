from django.urls import path
from .views import UserProfileAPIView, LeaderboardAPIView

urlpatterns = [
    path('profile/', UserProfileAPIView.as_view(), name='user_profile_api'),
    path('leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard_api'),
]