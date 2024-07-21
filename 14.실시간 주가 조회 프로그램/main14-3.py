import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_stock_price(stock_code):
    url = f"https://finance.naver.com/item/main.naver?code={stock_code}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "웹 페이지를 불러오는 데 실패했습니다."

    soup = BeautifulSoup(response.text, 'html.parser')
    price_tag = soup.select_one('p.no_today span.blind')

    if price_tag:
        return price_tag.text.strip().replace(',', '')  # 쉼표 제거
    else:
        return "주식 정보를 찾을 수 없습니다."

def on_submit():
    stock_code = entry.get()
    price = get_stock_price(stock_code)
    messagebox.showinfo("주식 금액", f"{stock_code}의 주식 금액: {price}원")

# GUI 설정
root = tk.Tk()
root.title("주식 금액 조회기")

# 입력 필드
label = tk.Label(root, text="종목번호를 입력하세요:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

# 제출 버튼
submit_button = tk.Button(root, text="조회", command=on_submit)
submit_button.pack(pady=20)

# GUI 루프 시작
root.mainloop()
