import MySQLdb
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from io import BytesIO
from finance_visualizer.views import FinancialDataAPIView, get_sorted_data
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement

class FinancialDataAPITestCase(APITestCase):
    databases = {'default', 'financial_data'}

    def test_get_financial_data(self):
        """
        測試 API 能否根據請求的 company_id, report_type 和 data_field 返回正確的數據。
        """
        company_id = '2880'
        report_type = 'indicator'
        data_field = 'ROA－綜合損益'
        
        view_instance = FinancialDataAPIView()
        model_field = view_instance.get_python_field_name(FinancialIndicator, data_field)
        
        if model_field is None:
            self.fail(f"未找到對應的模型字段: {data_field}")

        url = reverse('financial_data_api')
        response = self.client.get(url, {
            'company_id': company_id,
            'report_type': report_type,
            'data_field': data_field
        })

        print("Response status:", response.status_code)
        print("Response content:", response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertIn(company_id, response_data)
        self.assertIn(report_type, response_data[company_id])

        data_list = response_data[company_id][report_type][0]
        self.assertIsInstance(data_list, list)

        for item in data_list:
            self.assertIn("year_month", item)
            self.assertIn(data_field, item)

        db_data = list(
            FinancialIndicator.objects.filter(company_id=company_id)
            .order_by('year_month')
            .values('year_month', model_field)
        )

        expected_data = [
            {
                "year_month": item['year_month'],
                data_field: item[model_field]
            }
            for item in db_data
        ]

        sorted_expected_data = get_sorted_data(expected_data, model_field)
        self.assertEqual(data_list, sorted_expected_data)

    def tearDown(self):
        pass