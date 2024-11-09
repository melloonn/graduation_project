# finance_visualizer/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement
from .serializers import IndicatorSerializer, BalanceSheetSerializer, IncomeStatementSerializer, CashFlowStatementSerializer
import io
import base64
#from .langchain_utils import analyze_financial_data  
import re
from django.db.models import F
from rest_framework import serializers
from .utils import get_python_field_name

def get_sorted_data(data, db_field_name):
    month_order = ['Mar', 'Jun', 'Sep', 'Dec']

    def sort_key(item):
        year, month_str = item['year_month'].split('-')
        month_index = month_order.index(month_str)
        return (int(year), month_index)

    return sorted(data, key=sort_key)

class FinancialDataAPIView(APIView):
    def get(self, request, format=None):
        company_ids = request.GET.getlist('company_id')
        report_types = request.GET.getlist('report_type')
        data_fields = request.GET.getlist('data_field')

        # Debug: print incoming parameters
        print("Incoming request parameters:")
        print("Company IDs:", company_ids)
        print("Report Types:", report_types)
        print("Data Fields:", data_fields)

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
                    print(f"Unknown report type: {report_type}")
                    return Response({"error": f"未知的報告類型 '{report_type}'"}, status=status.HTTP_400_BAD_REQUEST)

                model_class, serializer_class = model_classes.get(report_type)

                for data_field in data_fields:
                    db_field_name = self.get_python_field_name(model_class, data_field)
                    print(f"Data field '{data_field}' mapped to database field '{db_field_name}'")

                    if not db_field_name:
                        return Response({"error": f"未知的 data_field: '{data_field}'"}, status=status.HTTP_400_BAD_REQUEST)

                    try:
                        data = model_class.objects.filter(company_id=company_id).order_by('year_month').values('year_month', db_field_name)

                        # Debug: check if data exists for the query
                        if not data.exists():
                            print(f"No data found for company_id {company_id} in report type {report_type}")
                            return Response({"error": f"未找到 {company_id} 的數據"}, status=status.HTTP_404_NOT_FOUND)

                        sorted_data = get_sorted_data(data, db_field_name)

                        if report_type not in response_data[company_id]:
                            response_data[company_id][report_type] = []

                        response_data[company_id][report_type].append([
                            {
                                "year_month": item['year_month'],
                                data_field: item[db_field_name]
                            } for item in sorted_data
                        ])

                    except Exception as e:
                        print(f"Error during data query or serialization: {e}")
                        return Response({"error": f"資料查詢或序列化出錯: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data, status=status.HTTP_200_OK)
    def get_python_field_name(self, model_class, db_column_name):
        for field in model_class._meta.fields:
            if field.db_column == db_column_name:
                return field.name
        print(f"Could not find matching field for db_column_name '{db_column_name}'")
        return None


# class FinancialIndicatorSummaryAPIView(APIView):
#     def post(self, request, format=None):
#         data = request.data.get('data')
#         if not data:
#             return Response({"error": "缺少必要的數據"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             analysis_result = analyze_financial_data(data)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         chart = self.generate_chart(serialized_data, data_field)
#         return Response({"chart": chart, "data": serialized_data})



class FinancialIndicatorSummaryAPIView(APIView):
    def post(self, request, format=None):
        data = request.data.get('data')
        if not data:
            return Response({"error": "缺少必要的數據"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            analysis_result = analyze_financial_data(data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"analysis": analysis_result})


class TopFieldAPIView(APIView):
    def get(self, request):
        """
        根據前端傳遞的 db_column_name（中文欄位名稱），返回該欄位排序後的前五筆數據，並提取年份。
        """
        # 從前端接收欄位名稱（中文）
        db_column_name = request.GET.get('field_name')

        if not db_column_name:
            return Response({"error": "缺少必要的參數 'field_name'"}, status=status.HTTP_400_BAD_REQUEST)

        # 呼叫 get_python_field_name 來獲取模型和欄位資訊
        target_model, python_field_name = self.get_python_field_name(db_column_name)

        if not target_model or not python_field_name:
            return Response({"error": f"欄位 '{db_column_name}' 在任何表中都不存在。"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 按字段排序並取得前五筆數據
            top_records = target_model.objects.values('company_id', 'name', 'year_month', python_field_name).order_by(F(python_field_name).desc())[:5]

            # 構造返回的 JSON 數據，提取年份
            response_data = [
                {
                    "company_id": record['company_id'],
                    "name": record['name'],
                    "year": record['year_month'].split('-')[0],  # 提取年份
                    "month": record['year_month'].split('-')[1],  # 可選，提取月份
                    db_column_name: record[python_field_name]  # 使用 Python 欄位名稱直接訪問字典值
                }
                for record in top_records
            ]

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"查詢數據時出錯: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_python_field_name(self, db_column_name):
        """
        根據資料庫欄位名稱（中文名稱），自動遍歷所有模型，
        返回欄位所屬的模型類和 Python 欄位名稱。
        """
        model_classes = [BalanceSheet, IncomeStatement, CashFlowStatement, FinancialIndicator]

        for model_class in model_classes:
            for field in model_class._meta.fields:
                if field.db_column == db_column_name:
                    return model_class, field.name  # 返回模型類和欄位名稱

        print(f"找不到對應的欄位名稱 '{db_column_name}'")
        return None, None