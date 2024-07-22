import time
import schedule
from plyer import notification

def show_notification():
    notification.notify(
        title="알림",
        message="회의시작 10분전입니다.",
        app_name='회의 알림 프로그램',
        timeout=10
    )
    print("알림이 출력되었습니다.")

# 알림을 설정할 요일과 시간
schedule.every().monday.at("09:50").do(show_notification)
schedule.every().wednesday.at("09:50").do(show_notification)
schedule.every().friday.at("09:50").do(show_notification)

print("알림 프로그램이 시작되었습니다.")

# 계속 실행
while True:
    schedule.run_pending()
    time.sleep(1)
