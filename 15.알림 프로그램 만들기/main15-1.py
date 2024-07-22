from plyer import notification

# 알림 제목과 메세지 설정
title = "알림 제목"
message = "이것은 알림 메세지입니다."

# 알림 출력
notification.notify(
    title=title,
    message=message,
    app_name='알림 프로그램', # 알림을 보낸 앱의 이름
    timeout=10 # 알림이 10초 후에 사라짐
)

print("알림이 출력되었습니다.")