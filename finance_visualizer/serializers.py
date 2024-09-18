from rest_framework import serializers

# 定義四個不同的序列化器，分別對應四種報表模型
class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # 這裡的模型將在使用時動態設置
        fields = '__all__'

class BalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # 這裡的模型將在使用時動態設置
        fields = '__all__'

class IncomeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # 這裡的模型將在使用時動態設置
        fields = '__all__'

class CashFlowStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # 這裡的模型將在使用時動態設置
        fields = '__all__'