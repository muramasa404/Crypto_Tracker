from get_economic_data import get_economic_data
from get_news_data import get_news_data

def update_readme():
    economic_data = get_economic_data()
    news_data = get_news_data()

    # README.md 업데이트 부분
    with open("README.md", "r") as file:  # 상위 폴더에 있는 README.md 파일을 열기
        content = file.read()

    # 경제 지표와 뉴스 데이터를 마크다운 형식으로 변환하여 삽입
    economic_data_md = "## 경제 지표\n\n<!-- ECONOMIC-DATA-START -->\n"
    economic_data_md += f"GDP: {economic_data}\n"
    economic_data_md += "<!-- ECONOMIC-DATA-END -->\n"

    news_data_md = "## 최신 경제 뉴스\n\n<!-- NEWS-START -->\n"
    for article in news_data["articles"]:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        news_data_md += f"### {title}\n{description}\n[Read more]({url})\n\n"
    news_data_md += "<!-- NEWS-END -->\n"

    content = content.replace("<!-- ECONOMIC-DATA-START -->", economic_data_md)
    content = content.replace("<!-- NEWS-START -->", news_data_md)

    with open("README.md", "w") as file:
        file.write(content)

if __name__ == "__main__":
    update_readme()
