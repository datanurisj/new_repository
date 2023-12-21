import json
import re
import os

def remove_comments(json_string):
    # 정규 표현식을 사용하여 주석을 제거합니다.
    json_string = re.sub(r'//.*?$|/\*.*?\*/', '', json_string, flags=re.S)
    return json_string

# 입력 폴더 경로를 지정합니다.
input_folder_path = 'C:\\Users\\이우성\\Desktop\\work\\json 한국어 작업\\주석제거 폴더'

try:
    # 입력 폴더의 모든 파일에 대해 반복합니다.
    for file_name in os.listdir(input_folder_path):
        if file_name.endswith('.json'):
            # 입력 JSON 파일 경로를 지정합니다.
            input_file_path = os.path.join(input_folder_path, file_name)

            # 입력 JSON 파일을 UTF-8 인코딩으로 읽어 들입니다.
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                json_data = input_file.read()
            
            # 주석을 제거합니다.
            json_data = remove_comments(json_data)
            
            # 주석이 제거된 JSON 데이터를 파싱합니다.
            parsed_data = json.loads(json_data)
            
            # 주석이 제거된 JSON 데이터를 같은 파일로 다시 저장합니다.
            with open(input_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(parsed_data, output_file, ensure_ascii=False, indent=2)
    
    print("모든 JSON 파일의 주석이 제거되었습니다.")
except FileNotFoundError:
    print(f"'{input_folder_path}' 디렉토리를 찾을 수 없습니다. 디렉토리 경로를 확인하십시오.")
except json.JSONDecodeError:
    print("JSON 파일 파싱 중 오류가 발생했습니다. JSON 형식 확인 필요.")
except Exception as e:
    print(f"오류 발생: {str(e)}")
