from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# 加載 .env 文件中的環境變量
load_dotenv()

# 從 .env 文件中讀取 API Key
api_key = os.getenv('OPENAI_API_KEY')

# 檢查 API Key 是否正確加載
if api_key is None:
    raise ValueError("API Key not found. Please set OPENAI_API_KEY in your .env file.")
else:
    print(f"API Key loaded...")  # 只打印前幾個字符以保護隱私

# 從 prompt/indicator_summary_prompt.txt 文件中讀取 prompt_template
prompt_file_path = os.path.join(os.path.dirname(__file__), 'prompt', 'indicator_summary_prompt.txt')
with open(prompt_file_path, 'r', encoding='utf-8') as file:
    prompt_template = file.read()

# LangChain setup
prompt = ChatPromptTemplate.from_template(prompt_template)
output_parser = StrOutputParser()

llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

chain = prompt | llm | output_parser

def analyze_financial_data(data):
    data_for_analysis = {
        "data": data
    }
    analysis_result = chain.invoke(data_for_analysis)
    return analysis_result

# 測試代碼塊
if __name__ == "__main__":
    # 測試數據
    test_data = [
        {"year_month": "2023-03", "revenue_growth": 16.60},
        {"year_month": "2023-06", "revenue_growth": 21.88},
        {"year_month": "2023-09", "revenue_growth": 20.36},
        {"year_month": "2023-12", "revenue_growth": 21.69}
    ]

    # 調用 analyze_financial_data 函數
    result = analyze_financial_data(test_data)
    print("Analysis Result:")
    print(result)