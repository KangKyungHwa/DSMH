# 깃허브 연결
# git clone https://github.com/KangKyungHwa/DSMH/ : 명령프로프트에서 실행 
# pip install mysql-connector-python  :내 pc에 설치되지 않은경우 실행

# 단어구름 시각화를 위해 필요한 라이브러리 설치하기
# pip install wordcloud  :내 pc에 설치되지 않은경우 실행

import pandas as pd
import feedparser
import requests
import mysql.connector
import matplotlib.pyplot as plt
from wordcloud import WordCloud



# Google News RSS feed URL for Korean news
url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/121.0.0.0 Safari/537.36",
    "Accept": "application/rss+xml, application/xml;q=0.9,*/*;q=0.8"
}


# DataFrame에 저장할 데이터를 담을 리스트를 생성합니다.
news_data = []

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    feed = feedparser.parse(response.text)

    if not feed.feed:
        print("Error: RSS feed metadata not found.")
    else:
        print("Feed title:", feed.feed.get('title', 'No title'))

    if not feed.entries:
        print("Error: No articles found in feed.")
    else:
        print(f"Number of parsed articles: {len(feed.entries)}")
        print("\n--- Top 5 News Article Titles ---")


except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Error: {e}")



# feed.entries를 반복하여 각 기사의 정보를 추출
for entry in feed.entries:
    title = entry.get('title', '제목 없음')
    link = entry.get('link', '링크 없음')
    published = entry.get('published', '발행일 정보 없음')
    summary = entry.get('summary', '요약 정보 없음')

    news_data.append({
        'title': title,
        'link': link,
        'published': published,
        'summary': summary
    })

# 추출된 데이터를 사용하여 pandas DataFrame을 생성합니다.
df_news = pd.DataFrame(news_data)

# 생성된 DataFrame의 첫 5행을 출력하여 확인합니다.
print("--- 뉴스 기사 DataFrame ) ---")
print(df_news.head(50))

# DataFrame의 총 행 수를 출력합니다.
print(f"\nDataFrame에 저장된 총 뉴스 기사 수: {len(df_news)}개")



#불러온 기사제목들을 csv 파일로 저장하는 경우 아래와 같이 코딩
#한글이 저장될 때 깨지지 않도록 utf-8 로 인코딩해서 저장
#df_news.to_csv('google_news_articles.csv', index=False, encoding='utf-8')

#print("DataFrame이 'google_news_articles.csv' 파일로 성공적으로 저장되었습니다.")
#print("현재 사용하는 파일 탐색기에서 파일을 확인할 수 있습니다.")



#데이터베이스에 수집되어진 뉴스 기사들을 저장하기 위해 MySQL 데이터베이스에 연결

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="a1234",
    database="daily_news"
)

cursor = conn.cursor()

for _, row in df_news.iterrows():
    sql = """
    INSERT INTO news_table (title, link, published, summary)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        title = VALUES(title),
        published = VALUES(published),
        summary = VALUES(summary)
    """

    cursor.execute(sql, (
        row['title'],
        row['link'],
        row['published'],
        row['summary']
    ))

conn.commit()
cursor.close()
conn.close()

print("중복 제거 포함 저장 완료!")


# 단어구름 시각화를 위해 뉴스 기사 제목을 하나의 문자열로 결합

text = " ".join(df_news["title"].astype(str))



wc = WordCloud(
    font_path="C:/Windows/Fonts/malgun.ttf",
    background_color="white",
    width=800,
    height=600
).generate(text)

plt.figure(figsize=(10,6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()