from googletrans import Translator

# 파일 경로
input_file_path = "09.영어로된 문서를 한글로 자동번역/영어문서.txt"
output_file_path = "09.영어로된 문서를 한글로 자동번역/한글번역.txt"

# Translator 객체 생성
translator = Translator()

# 영어 문서 읽기
with open(input_file_path, 'r', encoding='utf-8') as file:
    english_text = file.read()

# 영어 문서를 한국어로 번역
translated = translator.translate(english_text, src='en', dest='ko')

# 번역된 문서 쓰기
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(translated.text)

print("번역이 완료되었습니다. 번역된 파일은 다음 경로에 저장되었습니다.", output_file_path)