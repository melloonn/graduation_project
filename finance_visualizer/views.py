# finance_visualizer/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement
from .serializers import IndicatorSerializer, BalanceSheetSerializer, IncomeStatementSerializer, CashFlowStatementSerializer
import matplotlib.pyplot as plt
import io
import base64
from .langchain_utils import analyze_financial_data  

class FinancialDataAPIView(APIView):
    def get(self, request, format=None):
        company_id = request.GET.get('company_id')
        year_month = request.GET.get('year_month')
        report_type = request.GET.get('report_type')
        data_field = request.GET.get('data_field')

        if not company_id or not year_month or not report_type or not data_field:
            return Response({"error": "缺少必要的參數"}, status=status.HTTP_400_BAD_REQUEST)

        model_classes = {
            'indicator': (FinancialIndicator, IndicatorSerializer),
            'balance_sheet': (BalanceSheet, BalanceSheetSerializer),
            'income_statement': (IncomeStatement, IncomeStatementSerializer),
            'cash_flow': (CashFlowStatement, CashFlowStatementSerializer)
        }

        model_class, serializer_class = model_classes.get(report_type)
        if not model_class:
            return Response({"error": "未知的報告類型"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = model_class.objects.filter(company_id=company_id, year_month=year_month).values('year_month', data_field)
            if not data:
                return Response({"error": "未找到數據"}, status=status.HTTP_404_NOT_FOUND)

            serializer_class.Meta.model = model_class  # 在這裡動態設置模型
            serializer = serializer_class(data, many=True)
            serialized_data = serializer.data
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        chart = self.generate_chart(serialized_data, data_field)
        return Response({"chart": chart, "data": serialized_data})

    def generate_chart(self, data, data_field):
        plt.figure(figsize=(10, 6))
        plt.plot([item['year_month'] for item in data], [item[data_field] for item in data], marker='o')
        plt.title(f'{data_field} over Time')
        plt.xlabel('Year/Month')
        plt.ylabel(data_field)
        plt.grid(True)

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic

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