import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경 변수 로드

API_KEY = os.getenv("NEWS_API_KEY")  # 환경 변수로부터 API 키 가져오기

def get_news_data():
    # url = f"https://newsapi.org/v2/everything?q=Apple&from=2025-02-05&sortBy=popularity&apiKey={API_KEY}"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    params = {
         'apiKey': API_KEY,
         'country':'us' 
    
    #     'q': 'economy',  # 경제 관련 뉴스
    #     'apiKey': API_KEY,
    #     'language': 'en',
    #     'pageSize': 5  # 최신 5개 뉴스만 가져오기
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

if __name__ == "__main__":
    news_data = get_news_data()
    print(news_data)  # 또는 뉴스 처리 후 출력
