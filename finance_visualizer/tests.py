import matplotlib.pyplot as plt
import MySQLdb

# # 連接 MySQL 資料庫
# db = MySQLdb.connect(host="localhost", user="root", passwd="Melloonn920709!", db="sys")
# cursor = db.cursor()

# # 執行 SQL 查詢
# cursor.execute("SELECT 名稱, 營業收入淨額, 營業費用 FROM 金控損益表")
# results = cursor.fetchall()

# # 將資料分類
# names = []
# revenues = []
# expenses = []

# for row in results:
#     names.append(row[0])
#     revenues.append(row[1])
#     expenses.append(row[2])

# # 關閉資料庫連接
# db.close()

# # 繪製條形圖
# plt.figure(figsize=(10, 5))
# plt.bar(names, revenues, color='blue', label='營業收入淨額')
# plt.bar(names, expenses, color='red', label='營業費用', alpha=0.7)
# plt.xlabel('公司名稱')
# plt.ylabel('金額')
# plt.title('公司營業收入與費用')
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement
from django.contrib.auth.models import User

class FinancialDataAPITests(APITestCase):
    def setUp(self):
        # 假設已有模擬數據
        FinancialIndicator.objects.create(company_id='1', year_month='2020-01', data_field_value=100)
        self.client = APIClient()
    
    def test_missing_parameters(self):
        """ 測試缺少參數的請求 """
        url = reverse('financial_data_api')
        response = self.client.get(url, {'company_id': '1'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unknown_report_type(self):
        """ 測試未知的報告類型 """
        url = reverse('financial_data_api')
        response = self.client.get(url, {'company_id': '1', 'year_month': '2020-01', 'report_type': 'unknown', 'data_field': 'data_field_value'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_data_not_found(self):
        """ 測試數據不存在的情況 """
        url = reverse('financial_data_api')
        response = self.client.get(url, {'company_id': '999', 'year_month': '2020-01', 'report_type': 'indicator', 'data_field': 'data_field_value'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_data_retrieval_and_chart_generation(self):
        """ 測試數據檢索和圖表生成 """
        url = reverse('financial_data_api')
        response = self.client.get(url, {'company_id': '1', 'year_month': '2020-01', 'report_type': 'indicator', 'data_field': 'data_field_value'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('chart', response.data)  # 確認響應中有圖表資料
