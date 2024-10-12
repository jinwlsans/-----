import xml.etree.ElementTree as ET

# XML 파일 경로 설정
xml_file_path = 'C:/Users/진정욱/Desktop/대회/Training/[Training 라벨링]underwater photo/bundle of ropes_002_00012.xml'

try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    tag_name = 'object'  # 개수를 세고 싶은 태그 이름
    count = len(root.findall(tag_name))  

    # 결과 출력
    print(f"'{tag_name}' 태그의 개수: {count}")

except FileNotFoundError:
    print(f"Error: 파일이 존재하지 않습니다: {xml_file_path}")
except ET.ParseError as e:
    print(f"XML 파싱 오류: {e}")
except Exception as e:
    print(f"오류 발생: {e}")
