from django.urls import path
from .views import FinancialDataAPIView, FinancialIndicatorSummaryAPIView

urlpatterns = [
    path('api/financial_data/', FinancialDataAPIView.as_view(), name='financial_data_api'),
    path('api/financial_indicator_summary/', FinancialIndicatorSummaryAPIView.as_view(), name='financial_indicator_summary_api'),
]
