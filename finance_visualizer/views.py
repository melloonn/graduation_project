from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement
from .serializers import IndicatorSerializer, BalanceSheetSerializer, IncomeStatementSerializer, CashFlowStatementSerializer
import io
import re
from django.db.models import F
from rest_framework import serializers

# 動態序列化器，根據需要的欄位進行序列化
# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         # 接收並處理傳遞的 'fields' 參數
#         fields = kwargs.pop('fields', None)
#         super().__init__(*args, **kwargs)

#         if fields:
#             # 如果指定了字段，就只保留指定的字段
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)
# 改順序function(年月)
def get_sorted_data(data, db_field_name):
    # 自定義月份順序
    month_order = ['Mar', 'Jun', 'Sep', 'Dec']

    # 提取年份和月份的排序邏輯
    def sort_key(item):
        # 解析 year_month
        year, month_str = item['year_month'].split('-')
        # 根據自定義順序確定排序位置
        month_index = month_order.index(month_str)
        # 返回排序鍵值，優先按年份排序，其次按自定義月份順序排序
        return (int(year), month_index)

    # 按年份和自定義月份順序排序
    return sorted(data, key=sort_key)

class FinancialDataAPIView(APIView):
    def get(self, request, format=None):
        company_ids = request.GET.getlist('company_id')
        report_types = request.GET.getlist('report_type')
        data_fields = request.GET.getlist('data_field')

        if not company_ids or not report_types or not data_fields:
            return Response({
                "error": "缺少必要的參數", 
                "company_ids": company_ids, 
                "report_types": report_types, 
                "data_fields": data_fields
            }, status=status.HTTP_400_BAD_REQUEST)

        response_data = {}

        for company_id in company_ids:
            response_data[company_id] = {}

            for report_type in report_types:
                model_classes = {
                    'indicator': (FinancialIndicator, IndicatorSerializer),
                    'balance_sheet': (BalanceSheet, BalanceSheetSerializer),
                    'income_statement': (IncomeStatement, IncomeStatementSerializer),
                    'cash_flow': (CashFlowStatement, CashFlowStatementSerializer)
                }

                if report_type not in model_classes:
                    return Response({"error": f"未知的報告類型 '{report_type}'"}, status=status.HTTP_400_BAD_REQUEST)

                model_class, serializer_class = model_classes.get(report_type)

                for data_field in data_fields:
                    db_field_name = self.get_python_field_name(model_class, data_field)
                    if not db_field_name:
                        return Response({"error": f"未知的 data_field: '{data_field}'"}, status=status.HTTP_400_BAD_REQUEST)

                    try:
                        data = model_class.objects.filter(company_id=company_id).order_by('year_month').values('year_month', db_field_name)

                        if not data.exists():
                            return Response({"error": f"未找到 {company_id} 的數據"}, status=status.HTTP_404_NOT_FOUND)

                        sorted_data = get_sorted_data(data, db_field_name)

                        # 構建符合 JSON 格式的回應，使用 year_month
                        if report_type not in response_data[company_id]:
                            response_data[company_id][report_type] = []

                        response_data[company_id][report_type].append([
                            {
                                "year_month": item['year_month'],
                                data_field: item[db_field_name]
                            } for item in sorted_data
                        ])

                    except Exception as e:
                        return Response({"error": f"資料查詢或序列化出錯: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data, status=status.HTTP_200_OK)

    def get_python_field_name(self, model_class, db_column_name):
        """
        根據數據庫欄位名稱，動態查找對應的 Python 字段名
        """
        for field in model_class._meta.fields:
            if field.db_column == db_column_name:
                return field.name
        return None