import os
import pandas as pd
from faker import Faker

# Faker 인스턴스 생성
fake = Faker()

# 데이터 저장을 위한 리스트 초기화
data = []

# 1000개의 가짜 데이터 생성
for _ in range(1000):
    name = fake.name()
    gender = fake.random_element(elements=('Male', 'Female'))
    email = fake.email()
    phone_number = fake.phone_number()
    
    # 데이터 리스트에 추가
    data.append({
        'Name': name,
        'Gender': gender,
        'Email': email,
        'Phone Number': phone_number
    })

# 데이터프레임 생성 
df = pd.DataFrame(data)

# 폴더 생성 (존재하지 않는 경우)
output_folder = '12.가짜 개인정보를 만들어 엑셀에 저장하기'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 엑셀 파일로 저장
output_file = os.path.join(output_folder, '개인정보.xlsx')
df.to_excel(output_file, index=False)

print(f"데이터가 {output_file}에 성공적으로 저장되었습니다.")