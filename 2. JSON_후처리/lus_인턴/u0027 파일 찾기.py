import glob
import json

# 폴더 경로를 지정하세요.
folder_path = 'C:\\Users\\이우성\\Desktop\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_R\\*'

# .json 파일들만 선택합니다.
json_files = glob.glob(f'{folder_path}.json')

for file_name in json_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        data_str = f.read()

    # 문자열에서 \u0027 값이 있는지 확인합니다.
    if '\\u0027' in data_str:
        print(f'The file {file_name} contains \\u0027')
