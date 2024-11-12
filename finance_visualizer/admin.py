from django.contrib import admin
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement, FinancialReportSummary

@admin.register(FinancialIndicator)
class FinancialIndicatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FinancialIndicator._meta.fields]
    search_fields = ('name', 'year_month')

@admin.register(IncomeStatement)
class IncomeStatementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in IncomeStatement._meta.fields]
    search_fields = ('name', 'year_month')

@admin.register(CashFlowStatement)
class CashFlowStatementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CashFlowStatement._meta.fields]
    search_fields = ('name', 'year_month')

@admin.register(BalanceSheet)
class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BalanceSheet._meta.fields]
    search_fields = ('name', 'year_month')

admin.site.register(FinancialReportSummary)