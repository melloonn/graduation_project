# # finance_visualizer/tests.py

# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from finance_visualizer.views import FinancialDataAPIView
# from .models import FinancialIndicator, BalanceSheet, IncomeStatement, CashFlowStatement

# class FinancialDataAPITestCase(APITestCase):
#     databases = {'default', 'financial_data'}  # 使用特定的資料庫

#     def test_get_financial_data_for_single_field(self):
#         """
#         測試 API 能否根據請求的 company_id, report_type 和 data_field 返回正確的數據格式。
#         """
#         # 設定測試參數
#         company_id = '1409'
#         report_type = 'balance_sheet'
#         data_field = '現金及約當現金'

#         # 獲取 API URL 並發送 GET 請求
#         url = reverse('financial_data_api')
#         response = self.client.get(url, {
#             'company_id': company_id,
#             'report_type': report_type,
#             'data_field': data_field
#         })

#         # 打印 API 返回內容和狀態碼以進行檢查
#         print("Request parameters:")
#         print(f"company_id: {company_id}")
#         print(f"report_type: {report_type}")
#         print(f"data_field: {data_field}")
#         print("Response status:", response.status_code)
#         print("Response content:", response.json())

#         # 驗證 API 返回的狀態碼是否為 200 (或您預期的其他狀態碼)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # 檢查返回的數據格式
#         response_data = response.json()
        
#         # 檢查返回的數據是否包含指定的公司 ID
#         self.assertIn(company_id, response_data)

#         # 檢查返回的數據是否包含指定的報表類型
#         report_data = response_data[company_id]
#         self.assertIn(report_type, report_data)

#         # 獲取報表數據列表
#         data_list = report_data[report_type]
#         self.assertIsInstance(data_list, list)

#         # 檢查報表數據列表中的每個項目
#         for item in data_list:
#             self.assertIn("year_month", item)
#             self.assertIn(data_field, item)

#     def tearDown(self):
#         """
#         測試結束後不進行數據刪除,直接從資料庫中獲取測試數據。
#         """
#         pass

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import BalanceSheet

class FinancialDataAPITestCase(APITestCase):
    databases = {'default', 'financial_data'}  # 使用特定的資料庫

    def setUp(self):
        """
        在測試開始前，為測試資料庫插入一筆公司 ID 為 1409 的數據。
        """
        BalanceSheet.objects.create(
            company_id=1409,
            name="新纖",
            year_month="19-Jun",
            cash_and_equivalents=7077472,
            # 添加其他必要的欄位並設置初始值
        )

    def test_get_financial_data_for_single_field(self):
        """
        測試 API 能否根據請求的 company_id, report_type 和 data_field 返回正確的數據格式。
        """
        # 設定測試參數
        company_id = '1409'
        report_type = 'balance_sheet'
        data_field = '現金及約當現金'  # 使用前端請求的欄位名稱

        # 獲取 API URL 並發送 GET 請求
        url = reverse('financial_data_api')  # 假設路由名稱為 'financial_data_api'
        response = self.client.get(url, {
            'company_id': company_id,
            'report_type': report_type,
            'data_field': data_field
        })

        # 打印 API 返回內容和狀態碼以進行檢查
        print("Request parameters:")
        print(f"company_id: {company_id}")
        print(f"report_type: {report_type}")
        print(f"data_field: {data_field}")
        print("Response status:", response.status_code)
        print("Response content:", response.json())

        # 驗證 API 返回的狀態碼是否為 200 (或你預期的其他狀態碼)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 檢查返回的數據格式
        response_data = response.json()
        
        # 檢查返回的數據是否包含指定的公司 ID
        self.assertIn(company_id, response_data)

        # 檢查返回的數據是否包含指定的報表類型
        report_data = response_data[company_id]
        self.assertIn(report_type, report_data)

        # 獲取報表數據列表並檢查嵌套結構
        data_list = report_data[report_type][0]  # 這裡取出內部列表
        self.assertIsInstance(data_list, list)

        # 檢查報表數據列表中的每個項目
        for item in data_list:
            self.assertIn("year_month", item)
            self.assertIn(data_field, item)

    def tearDown(self):
        """
        測試結束後不進行數據刪除,直接從資料庫中獲取測試數據。
        """
        pass