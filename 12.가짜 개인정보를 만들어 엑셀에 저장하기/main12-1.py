from faker import Faker

# Faker 인스턴스 생성
fake = Faker()

# 한국어로 설정
Faker.seed(0)
fake_kr = Faker('ko_KR')

# 가짜 개인정보 생성
name = fake_kr.name()
address = fake_kr.address()
phone_number = fake_kr.phone_number()
email = fake_kr.email()
job = fake_kr.job()

# 생성된 가짜 개인정보 출력
print(f"이름: {name}")
print(f"주소: {address}")
print(f"전화번호: {phone_number}")
print(f"이메일: {email}")
print(f"직업: {job}")