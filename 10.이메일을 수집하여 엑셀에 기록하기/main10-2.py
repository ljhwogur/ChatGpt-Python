import requests
from bs4 import BeautifulSoup
import re
import openpyxl
import os

def extract_emails(url):
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
    
    # 중복된 이메일 주소 제거
    emails = list(set(emails))
    
    return emails

def save_emails_to_excel(emails, file_path):
    # 엑셀 파일 생성
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Emails"
    
    # 헤더 추가
    ws.append(["Email"])
    
    # 이메일 주소 추가
    for email in emails:
        ws.append([email])
        
    # 디렉토리가 존재하지 않으면 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 엑셀 파일 저장
    wb.save(file_path)
    print(f"Emails have been saved to {file_path}")
    
# 예제 URL
url = "https://n.news.naver.com/article/629/0000300311?cds=news_media_pc&type=editn"

# 이메일 주소 추출
emails = extract_emails(url)

# 결과 출력 및 엑셀 파일에 저장
if emails:
    print("Emails found:")
    for email in emails:
        print(email)
    file_path = "10.이메일을 수집하여 엑셀에 기록하기/이메일.xlsx"
    save_emails_to_excel(emails, file_path)
else:
    print("No emails found.")