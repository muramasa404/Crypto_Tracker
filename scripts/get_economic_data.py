import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경 변수 로드

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")  # 환경 변수로부터 API 키 가져오기

def get_economic_data():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}"
    params = {
        'function': 'REAL_GDP',  # 실질 GDP 데이터
        'apikey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

if __name__ == "__main__":
    economic_data = get_economic_data()
    print(economic_data)  # 또는 데이터 처리 후 출력
