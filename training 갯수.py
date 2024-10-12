import os

# 이미지가 저장된 디렉토리 경로
directory_path = 'C:/Users/진정욱/Desktop/대회/Training/[Training 원천]underwater photo'

image_extensions = ('.jpg')  # 이미지 파일 확장자 목록

image_count = 0  # 이미지 파일 수 초기화

for filename in os.listdir(directory_path):  # 디렉토리 내의 모든 파일을 확인
      
    if filename.lower().endswith(image_extensions):  
        image_count += 1

print(f"이미지의 수: {image_count}")  # 이미지 파일 수 출력
