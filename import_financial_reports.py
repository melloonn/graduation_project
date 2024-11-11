import os
import django

# 設定Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend_FinalProject.settings')
django.setup()


from finance_visualizer.models import FinancialReportSummary

# 設定txt檔案的目錄
txt_directory = '/Users/rex/LLM_finance question/financial_report_summaries'

# 讀取目錄中的所有txt檔案
for filename in os.listdir(txt_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(txt_directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            title = filename.replace('.txt', '')  # 使用檔名作為標題

            # 將資料儲存到資料庫
            FinancialReportSummary.objects.create(title=title, content=content)

print("資料匯入完成！")