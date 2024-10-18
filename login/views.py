from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .models import User
from .serializers import UserSerializer
# drf-yasg 用於 Swagger 支持
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# 自定義的 Google 登入視圖
from social_django.utils import psa
from rest_framework.decorators import api_view

class LoginView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_description="使用者登入，提供電子郵件和密碼以獲取 JWT access 和 refresh token。",
        tags=['Authentication'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='使用者電子郵件', example='user@example.com'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='使用者密碼', example='password123'),
            },
            required=['email', 'password'],
        ),
        responses={
            200: openapi.Response(
                description='登入成功',
                examples={
                    'application/json': {
                        'refresh': 'string (refresh token)',
                        'access': 'string (access token)',
                    }
                }
            ),
            401: openapi.Response(
                description='認證失敗，無效的憑證。',
                examples={
                    'application/json': {
                        "detail": "Invalid credentials"
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('username')
        password = request.data.get('password')

        # 查找對應的使用者
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "Invalid email"}, status=status.HTTP_401_UNAUTHORIZED)

        # 驗證密碼
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="使用者登出，必須提供有效的 access token。",
        tags=['Authentication'],
        responses={
            204: openapi.Response(
                description='登出成功，無內容回應。'
            ),
            401: openapi.Response(
                description='未授權，缺少或無效的 token。',
                examples={
                    'application/json': {
                        "detail": "Authentication credentials were not provided."
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @swagger_auto_schema(
        operation_description="用戶註冊，提供使用者名稱、電子郵件和密碼來創建新的帳戶。",
        tags=['Authentication'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='使用者名稱', example='user123'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='電子郵件地址', example='user@example.com'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='使用者密碼', example='password123'),
            },
            required=['username', 'email', 'password'],
        ),
        responses={
            201: openapi.Response(
                description='註冊成功',
                examples={
                    'application/json': {
                        'id': 1,
                        'username': 'user123',
                        'email': 'user@example.com'
                    }
                }
            ),
            400: openapi.Response(
                description='請求格式錯誤或資料無效',
                examples={
                    'application/json': {
                        "username": ["此欄位不能為空。"],
                        "password": ["密碼太短，請至少輸入8位。"]
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        #將輸入值抓成可以改動的字典格式
        data = request.data.copy()
        #把密碼hash並存回data字典
        data['password'] = make_password(data['password'])
        #序列化器負責對資料進行驗證儲存
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Google 登入的視圖
@swagger_auto_schema(
    method='post',
    operation_description="使用 Google OAuth 登入，提供 Google 的 OAuth token 來獲取 JWT token。",
    tags=['Authentication'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'token': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='從 Google 獲取的 OAuth token', 
                example='ya29.a0ARrdaM9...',
            ),
        },
        required=['token'],
    ),
    responses={
        200: openapi.Response(
            description='登入成功，返回 JWT token 和使用者資訊',
            examples={
                'application/json': {
                    'refresh': 'string (refresh token)',
                    'access': 'string (access token)',
                    'user': {
                        'id': 1,
                        'username': 'user123',
                        'email': 'user@example.com',
                    }
                }
            }
        ),
        400: openapi.Response(
            description='缺少 token 或請求格式錯誤。',
            examples={
                'application/json': {
                    'error': 'No token provided.'
                }
            }
        ),
        401: openapi.Response(
            description='驗證失敗，無效的 token。',
            examples={
                'application/json': {
                    'error': 'Authentication failed.'
                }
            }
        ),
    }
)
@psa('social:complete')
@api_view(['POST'])
def google_login(request, backend):
    token = request.data.get('token')
    if not token:
        return Response({'error': 'No token provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 驗證 Google token 並獲取對應的使用者
    user = request.backend.do_auth(token)
    if user:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)

class ForgotPasswordView(APIView):
    @swagger_auto_schema(
        operation_description="用戶忘記密碼，提供電子郵件地址，系統會發送一個密碼重設連結到該電子郵件。",
        tags=['Authentication'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING, 
                    description='使用者的電子郵件地址', 
                    example='user@example.com',
                ),
            },
            required=['email'],
        ),
        responses={
            200: openapi.Response(
                description='成功發送密碼重設郵件。',
                examples={
                    'application/json': {
                        'detail': 'Password reset email has been sent.'
                    }
                }
            ),
            404: openapi.Response(
                description='未找到對應電子郵件的使用者。',
                examples={
                    'application/json': {
                        'detail': 'User with this email does not exist.'
                    }
                }
            ),
        }
    )
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        #生成一個重置密碼的token
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}&uid={user.id}"
        
        #內建發送信件功能
        send_mail(
            'Reset Your Password',
            f'Click the link below to reset your password:\n{reset_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        
        return Response({"detail": "Password reset email has been sent."}, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    @swagger_auto_schema(
        operation_description="重設密碼，提供重設密碼的 token、使用者 ID 和新密碼。",
        tags=['Authentication'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='重設密碼的驗證 token',
                    example='eJxsNzIw...'
                ),
                'uid': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='使用者 ID',
                    example=1
                ),
                'new_password': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='新的密碼',
                    example='newpassword123'
                ),
            },
            required=['token', 'uid', 'new_password'],
        ),
        responses={
            200: openapi.Response(
                description='密碼重設成功',
                examples={
                    'application/json': {
                        'detail': 'Password has been reset successfully.'
                    }
                }
            ),
            400: openapi.Response(
                description='無效或過期的 token。',
                examples={
                    'application/json': {
                        'detail': 'Invalid or expired token.'
                    }
                }
            ),
            404: openapi.Response(
                description='使用者 ID 無效。',
                examples={
                    'application/json': {
                        'detail': 'Invalid user ID.'
                    }
                }
            ),
        }
    )
    def post(self, request):
        token = request.data.get('token')
        uid = request.data.get('uid')
        new_password = request.data.get('new_password')
        
        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return Response({"detail": "Invalid user ID."}, status=status.HTTP_404_NOT_FOUND)
        
        token_generator = PasswordResetTokenGenerator()
        if token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)