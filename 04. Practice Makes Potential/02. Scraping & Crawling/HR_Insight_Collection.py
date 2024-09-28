# HR Insight Collecting basics with requests, bs4

import requests
from bs4 import BeautifulSoup

url = "http://www.findjob.co.kr/job/guide/jobNewsList.asp"
response = requests.get(url)

contents = response.text
soup = BeautifulSoup(contents, "html.parser")

title = soup.find("title")
print(f"기사 소스 : {title.text}")

div_group = soup.find_all("a", class_="lineItem-full")

num = 0  # 기사 자료 순서 매기기
for news in div_group:
    num += 1
    article_title = news.find("dt", class_="lineItem-full__txt__tit")
    article_summary = news.find("dd", class_="lineItem-full__txt__con")
    article_time = news.find("span", class_="date")

    print(
        f"""{num}번 기사
기사 타이틀: {article_title.text}
기사 요약: {article_summary.text}
발행 일자: {article_time.text}"""
    )
    print()
