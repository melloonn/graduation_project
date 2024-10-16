from django.urls import path
from .views import LoginView, LogoutView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),  # 使用自定義的 LoginView
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/register/', RegisterView.as_view(), name='register'),  # 添加註冊路由
]


