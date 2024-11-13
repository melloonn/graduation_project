from django.urls import path
from .views import FinancialDataAPIView, FinancialIndicatorSummaryAPIView, TopFieldAPIView, FinancialSummaryAPIView

urlpatterns = [
    path('api/top_field/', TopFieldAPIView.as_view(), name='top_field'),
    path('api/financial_data/', FinancialDataAPIView.as_view(), name='financial_data_api'),
    path('api/financial_indicator_summary/', FinancialIndicatorSummaryAPIView.as_view(), name='financial_indicator_summary_api'),
    path('api/summary/', FinancialSummaryAPIView.as_view(), name='financial_summary'),
]
