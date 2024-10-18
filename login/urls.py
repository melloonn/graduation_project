from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    RegisterView,
    google_login,
    ForgotPasswordView,
    ResetPasswordView,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 註冊 API
    path('login/', LoginView.as_view(), name='login'),  # 登入 API
    path('logout/', LogoutView.as_view(), name='logout'),  # 登出 API
    path('login/google/<str:backend>/', google_login, name='google-login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),  # 忘記密碼 API
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),  # 重設密碼 API
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]


