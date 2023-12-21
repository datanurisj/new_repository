import glob
from tqdm import tqdm   
from time import sleep

# 폴더 경로를 지정
folder_path = 'C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206\\증권_T\\*'       # 라이프_L, 부동산_R, 산업_I, 스포츠_S, 연예_E, 오피니언_O, 증권_T

# .json 파일들만 선택
json_files = glob.glob(f'{folder_path}.json')

for file_name in tqdm(json_files):
    with open(file_name, 'r', encoding='utf-8') as f:
        data_str = f.read()

    # 문자열에서 \n 값 삭제
    modified_data_str = data_str.replace('\\n', '')


    # 수정된 데이터를 원본 파일에 다시 씀
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(modified_data_str)
    sleep(0.1)
