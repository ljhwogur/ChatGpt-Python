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

def main():
    stock_code = input("종목번호를 입력하세요: ")
    price = get_stock_price(stock_code)
    print(f"{stock_code}의 주식 금액: {price}원")

if __name__ == "__main__":
    main()
