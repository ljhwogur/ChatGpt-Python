import requests
from bs4 import BeautifulSoup
import re

def extract_emils(url):
    # 웹페이지 내용 가져오기
    response = requests.get(url)
    
    # 요청이 성공했는지 확인
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    # 웹페이지 내용 파싱
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 정규 표현식을 사용하여 이메일 주소 추출
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, soup.get_text())
    
    # 중복된 이메을 주소 제거
    emails = list(set(emails))
    
    return emails

# 예제 URL
url = "https://n.news.naver.com/article/629/0000300311?cds=news_media_pc&type=editn"
# 이메일 주소 추출
emails = extract_emils(url)

# 결과 출력
if emails:
    print("Emails found:")
    for email in emails:
        print(email)
else:
    print("No emails found.")