import yfinance as yf
import time

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period='1d') # 최근 1일 데이터 가져오기
    return data['Close'][-1] # 최근 종가 반환

def main():
    ticker = input("조회할 주식의 티커(symbol)를 입력하세요: ")
    
    while True:
        try:
            price = get_stock_price(ticker)
            print(f"{ticker}의 현재 주가는: {price:.2f} USD")
            time.sleep(10) # 10초마다 업데이트
        except Exception as e:
            print(f"오류 발생: {e}")
            break

if __name__ == "__main__":
    main()