from django.urls import path
from .views import FinancialDataAPIView

urlpatterns = [
    path('api/financial_data/', FinancialDataAPIView.as_view(), name='financial_data_api'),
]