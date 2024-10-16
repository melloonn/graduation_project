from rest_framework import serializers
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement

# 定義四個不同的序列化器，分別對應四種報表模型
class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialIndicator  # 對應 FinancialIndicator 模型
        fields = '__all__'  # 序列化模型的所有字段

class BalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceSheet  # 對應 BalanceSheet 模型
        fields = '__all__'

class IncomeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeStatement  # 對應 IncomeStatement 模型
        fields = '__all__'

class CashFlowStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlowStatement  # 對應 CashFlowStatement 模型
        fields = '__all__'