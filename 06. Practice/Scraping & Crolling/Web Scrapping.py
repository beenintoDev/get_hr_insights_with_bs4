import requests
from bs4 import BeautifulSoup

num = 1

url = "https://magazine.hankyung.com/job-joy/tag/20210224174448473"
response = requests.get(url)
print(f"서버 요청 결과는? {response.status_code} 입니다.")
print()

html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
all_news_div = soup.find_all("div", class_="news-cont")

# 각각의 div에서 각각의 요소를 추출
for div in all_news_div:
    title = div.find(
        "h3", class_="news-tit"
    )  # h3 태그와 특정 클래스를 활용하여 기사 타이틀을 추출
    image = div.find(
        "img"
    )  # img 태그를 활용하여 이미지 태그 이하 내용을 추출 (scr + alt)

    # 기사로 이동할 수 있는 a 태그에서 href 속성 추출
    hyperlink = div.find("a")  # 링크를 찾기 위해 a 태그를 검색

    if title:
        print(f"기사 {num}:")
        num += 1
        print(f"제목{title.text.strip()}")  # 제목 텍스트 출력 (앞뒤 공백 제거)
    if image:
        print(image.get("src"))
        if (
            image.get("alt") != title.text.strip()
        ):  # 이미지 설명 텍스트가 title과 동일하다면 생략함
            print(f'이미지에 대한 설명 : {image.get("alt")}')
    if hyperlink and hyperlink.get("href"):
        print(f"기사원문: {hyperlink.get('href')}")
