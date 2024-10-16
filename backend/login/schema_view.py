# login/schema_view.py
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Login API Documentation",
        default_version='v1',
        description="API documentation for the login system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[path('login/', include('login.urls'))]
)
