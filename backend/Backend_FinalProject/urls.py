"""
URL configuration for Backend_FinalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Login 系統的 Swagger 設置
login_schema_view = get_schema_view(
    openapi.Info(
        title="Login API Documentation",
        default_version='v1',
        description="API documentation for the login system",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # urlconf='login.urls',
    # patterns=[path('login/', include('login.urls'))],
    url='http://127.0.0.1:8000/',
)

finance_schema_view = get_schema_view(
    openapi.Info(
        title="Finance Visualizer API Documentation",
        default_version='v1',
        description="API documentation for the finance visualizer system",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@finance.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # urlconf='finance_visualizer.urls',  # 指定該Swagger配置的URL配置檔案
    # patterns=[path('api/', include('finance_visualizer.urls'))],  # 引入finance_visualizer的URL
    url='http://127.0.0.1:8000/',
)

# 其他 API 的 Swagger 設置
# general_schema_view = get_schema_view(
#     openapi.Info(
#         title="General API Documentation",
#         default_version='v1',
#         description="General API documentation",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('swagger/login/', login_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-login'),
    # path('swagger/general/', general_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-general'),
    path('', include('finance_visualizer.urls')),
    path('swagger/finance/', finance_schema_view.with_ui('swagger', cache_timeout=0), name='finance-schema-swagger-ui'),
]
