from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement
from .serializers import IndicatorSerializer, BalanceSheetSerializer, IncomeStatementSerializer, CashFlowStatementSerializer
import matplotlib.pyplot as plt
import io
import base64
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
#改順序function(年月)
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

# 在視圖中使用這個序列化器
class FinancialDataAPIView(APIView):
    def get(self, request, format=None):
        # 從請求中獲取參數
        company_id = request.GET.get('company_id')
        report_type = request.GET.get('report_type')
        data_field = request.GET.get('data_field')

        # 檢查必要參數
        if not company_id or not report_type or not data_field:
            return Response({
                "error": "缺少必要的參數", 
                "company_id": company_id, 
                "report_type": report_type, 
                "data_field": data_field
            }, status=status.HTTP_400_BAD_REQUEST)

        model_classes = {
            'indicator': (FinancialIndicator, IndicatorSerializer),
            'balance_sheet': (BalanceSheet, BalanceSheetSerializer),
            'income_statement': (IncomeStatement, IncomeStatementSerializer),
            'cash_flow': (CashFlowStatement, CashFlowStatementSerializer)
        }

        if report_type not in model_classes:
            return Response({"error": f"未知的報告類型 '{report_type}'"}, status=status.HTTP_400_BAD_REQUEST)

        model_class, serializer_class = model_classes.get(report_type)

        # 動態查找 Python 字段名
        db_field_name = self.get_python_field_name(model_class, data_field)
        if not db_field_name:
            return Response({"error": f"未知的 data_field: '{data_field}'"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 查詢符合條件的資料，只取所需欄位
            
            data = model_class.objects.filter(company_id=company_id).order_by('year_month').values('company_id', 'year_month', db_field_name)

            if not data.exists():
                return Response({"error": "未找到數據"}, status=status.HTTP_404_NOT_FOUND)
            #看data回傳格式
            # 自定義排序
            sorted_data = get_sorted_data(data, db_field_name)

            return Response({"data": list(sorted_data)})
            # 動態序列化僅需要的字段
            # serializer = DynamicFieldsModelSerializer(data, fields=['company_id', 'year_month', db_field_name], many=True)
            # serialized_data = serializer.data

        except Exception as e:
            return Response({"error": f"資料查詢或序列化出錯: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            # 生成圖表
            # chart = self.generate_chart(serialized_data, db_field_name)
            chart = self.generate_chart(list(sorted_data), db_field_name)
            if not chart:
                print("圖表生成失敗")
                return Response({"error": "圖表生成失敗"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        except Exception as e:
            print(f"生成圖表出錯: {str(e)}")
            return Response({"error": f"生成圖表出錯: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        print("圖表成功生成並包含在返回中")
        return Response({"chart": chart, "data": list(sorted_data)})

    def get_python_field_name(self, model_class, db_column_name):
        """
        根據數據庫欄位名稱，動態查找對應的 Python 字段名
        """
        # 添加打印以查看 db_column_name 是否正確
        print(f"正在查找對應的 Python 字段名，目標 db_column: {db_column_name}")
        
        for field in model_class._meta.fields:
            # 添加打印以查看每個字段的 db_column 名稱
            print(f"檢查字段: {field.name}, db_column: {field.db_column}")
            
            if field.db_column == db_column_name:
                print(f"找到匹配的字段名: {field.name}")
                return field.name
        print(f"未找到匹配的 db_column: {db_column_name}")
        return None


    def generate_chart(self, data, data_field):
        try:
            # 檢查數據的結構
            print(f"數據傳入 generate_chart: {data}")
            print(f"字段名稱: {data_field}")

            # 使用 'year_month' 作為 x 軸，'data_field' 的值作為 y 軸
            year_months = [item['year_month'] for item in data]
            values = [item[data_field] for item in data]

            print(f"x 軸數據: {year_months}")
            print(f"y 軸數據: {values}")

            plt.figure(figsize=(10, 6))
            plt.plot(year_months, values, marker='o')
            plt.title(f'{data_field} over Time')
            plt.xlabel('Year/Month')
            plt.ylabel(data_field)
            plt.xticks(rotation=45)
            plt.grid(True)

            # 保存圖表到內存
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            # 將圖表轉換為 base64
            graphic = base64.b64encode(image_png).decode('utf-8')
            return graphic

        except Exception as e:
            # 如果生成圖表失敗，打印錯誤訊息
            print(f"圖表生成出錯: {str(e)}")
            return None  # 如果生成失敗，返回 None