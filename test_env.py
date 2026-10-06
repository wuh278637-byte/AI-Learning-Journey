import os
from dotenv import load_dotenv

load_dotenv("D:/APP/.env")

api_key = os.getenv("AI_API_KEY")

print("读取结果：", bool(api_key))

if api_key:
    print("API Key 已成功读取！")