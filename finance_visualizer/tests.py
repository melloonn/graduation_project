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

# 
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from .models import BalanceSheet

# class FinancialDataAPITest(APITestCase):
#     databases = '__all__'  # 允許資料庫操作

#     def setUp(self):
#         BalanceSheet.objects.create(
#             code="2880",
#             name="華南金",
#             period="23-Dec",
#             cash_and_cash_equivalents=39596420,
#             accounts_receivable=18142617,
#             other_receivables=67252591,
#             property_plant_and_equipment=31978737,
#             goodwill_and_intangibles=919111,
#             right_of_use_assets=2268659,
#             investment_property_net=14863175,
#             other_non_current_assets=4594464,
#             total_assets=3869201779,
#             accounts_payable=16845968,
#             other_payables=48200920,
#             total_liabilities=3661389443,
#             common_stock=136427459,
#             capital_surplus=17761804,
#             retained_earnings=63895129,
#             other_equity=-10274310,
#             total_equity=207812336,
#             total_liabilities_and_equity=3869201779
#         )

#     def test_successful_data_retrieval(self):
#         url = reverse('financial_data')
#         response = self.client.get(url, {
#             'company_id': '2880',
#             'year_month': '23-Dec',
#             'report_type': 'balance_sheet',
#             'data_field': 'total_assets'
#         })

#         self.assertEqual(response.status_code, 200)
#         self.assertIn('data', response.data)
#         self.assertIn('chart', response.data)


#     def test_data_not_found(self):
#         url = reverse('financial_data')
#         response = self.client.get(url, {
#             'company_id': '9999',  # 不存在的公司ID
#             'year_month': '23-Dec',
#             'report_type': 'balance_sheet',
#             'data_field': 'total_assets'
#         })

#         self.assertEqual(response.status_code, 404)

#     def test_invalid_report_type(self):
#         url = reverse('financial_data')
#         response = self.client.get(url, {
#             'company_id': '2880',
#             'year_month': '23-Dec',
#             'report_type': 'invalid_report',  # 無效的報告類型
#             'data_field': 'total_assets'
#         })

#         self.assertEqual(response.status_code, 400)

#     def test_missing_parameters(self):
#         url = reverse('financial_data')
#         response = self.client.get(url, {
#             'company_id': '2880',
#             'report_type': 'balance_sheet',
#             'data_field': 'total_assets'
#         })

#         self.assertEqual(response.status_code, 400)

import matplotlib.pyplot as plt
import MySQLdb
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import base64
from io import BytesIO
import matplotlib.pyplot as plt

class FinancialDataAPITestCase(APITestCase):
    databases = {'default', 'financial_data'}  # 使用 MySQL 資料庫和 SQLite 資料庫

    def test_get_financial_data(self):
        """
        測試 API 能否根據請求的 company_id, report_type 和 data_field 返回正確的數據與折線圖。
        """
        # 設置前端傳入的模擬參數
        url = reverse('financial_data_api')  # 假設路由名稱為 'financial_data_api'
        response = self.client.get(url, {
            'company_id': 2880,  # 假設資料庫中存在這個公司 ID
            'report_type': 'indicator',  # 使用模型類型的小寫名稱
            'data_field': 'ROA－綜合損益'  # 對應 'ROA－綜合損益' 欄位
        })

        # 打印具體的 API 返回內容，幫助檢查問題
        print("Response status:", response.status_code)
        print("Response content:", response.json())

        # 測試 API 回傳狀態碼是否為 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 測試返回的數據是否正確
        response_data = response.json()

        # 確保數據字段存在
        self.assertIn('data', response_data)

        # 測試返回的具體數據，這裡的 `expected_data` 需要根據資料庫的實際數據進行配置
        # expected_data = [
        #     {'year_month': '2023-01', 'ROA－綜合損益': '5.12345'},
        #     {'year_month': '2023-04', 'ROA－綜合損益': '6.23456'},
        #     {'year_month': '2023-07', 'ROA－綜合損益': '7.34567'},
        #     {'year_month': '2023-10', 'ROA－綜合損益': '8.45678'},
        # ]
        # 這裡可以根據實際的數據進行校驗
        # self.assertEqual(response_data['data'], expected_data)

        # 確認圖表存在且為 Base64 字串
        self.assertIn('chart', response_data)
        chart_data = response_data.get('chart')

        if not chart_data:
            self.fail(f"圖表未生成或未包含在回應中: {response_data}")

        # 嘗試解碼 Base64 編碼的圖表，確保其為有效圖像
        try:
            decoded_image = base64.b64decode(chart_data)
            image = BytesIO(decoded_image)
            plt.imread(image)  # 測試能否讀取圖片，無法讀取則拋出錯誤
        except Exception as e:
            self.fail(f"圖表生成失敗: {e}")