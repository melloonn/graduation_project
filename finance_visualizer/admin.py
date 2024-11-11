from django.contrib import admin
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement, FinancialReportSummary
# Register your models here.

admin.site.register(FinancialIndicator)
admin.site.register(BalanceSheet)
admin.site.register(IncomeStatement)
admin.site.register(CashFlowStatement)
admin.site.register(FinancialReportSummary)