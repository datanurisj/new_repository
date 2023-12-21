# library
import os
import json
import pandas as pd
from tqdm import tqdm   
from time import sleep

# 삭제 파일 경로path
remove_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\01. 이벤트\\05. 이벤트 통폐합\\1. 통폐합_final\\한국어_최종_제외파일\\증권"  
file_list = os.listdir(remove_path)                                                                                                         # 라이프, 부동산, 산업, 스포츠, 연예, 오피니언, 증권
len(file_list)



# 전체 파일 경로
f_path = 'C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206\\증권_T\\'      # 라이프_L, 부동산_R, 산업_I, 스포츠_S, 연예_E, 오피니언_O, 증권_T
f_life_remove_list = os.listdir(f_path)     # 라이프 경로내 파일
len(f_life_remove_list)

count = 0
for file_name in file_list:
    file_path = os.path.join(f_path, file_name)
    if file_name in f_life_remove_list:
        os.remove(file_path)
        print(f'{file_name} 파일 삭제')
        count += 1
        print(count)
    else:
        print(f'{file_name} 파일을 찾을 수 없음')

