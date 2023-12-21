# library
import glob
import pandas as pd
from openpyxl import Workbook
import os
from os import path
import json
import copy
import shutil


# path
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\01. 이벤트\\05. 이벤트 통폐합\\1. 통폐합_final\\한국어_최종_제외파일_이었던것\\연예\\*"
#json_file = glob.glob(f'{path}.json')       # 경로 내 JSON파일 잡아냄       연예_E, 스포츠_S, 산업_I, 오피니언_O, 부동산_R, 증권_T, 라이프_L
#len(json_file)

vin = []
#for i in json_file:
#    print(i[125:166])
#    vin.append(i[125:166])
#    
#data = pd.DataFrame(vin)

#data

#data.to_excel('연예 2건.xlsx')


#### 파일 경로      # excel -> df -> list로 목록 추출
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_n값_리스트\\1065건\\"
file_name = '증권 462건.xlsx'         # 라이프 218건, 부동산 346건, 산업 3건, 스포츠 32건, 연예 2건, 오피니언 2건, 증권 462건
df = pd.read_excel(path + file_name)

print(df)

# df to list
df = df[0]
val_list = df.values.tolist()
val_list
val_list[0]
len(val_list)

# 데이터 목록 안에 val_list가 있으면 경로로 copy
origin = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_354건_후처리_231206\\이벤트_통폐합_1206_복사본\\trainning\\증권_T"
copy_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_n값_리스트\\증권"          # 라이프_L, 부동산_R, 산업_I, 스포츠_S, 연예_E, 오피니언_O, 증권_T

orgin_files = os.listdir(origin)
len(orgin_files)

# 복사
for file in orgin_files:
    if not os.path.exists(copy_path + '\\' + file):
        shutil.copy(origin + '\\' + file, copy_path + '\\' + file)
        
# 증권 n값 데이터가 있으면 해당 데이터만 생존, 나머지는 제거
c = 0
for i in val_list:
    print(i)
    c += 1
    print(c)
    
copy_files = os.listdir(copy_path)


#for i in val_list:
#    if i in copy_files:

for file in copy_files:
    if file not in val_list:
        os.remove(copy_path + '\\' + file)
        print(f"파일 '{file}을 삭제했습니다.")        

print("작업이 완료 되었습니다.")


# 각 목록 별 event_entity 개수 파악
file_data = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_n값_리스트\\증권"      # 라이프, 부동산, 산업, 스포츠, 연예, 오피니언, 증권
file_data_list = os.listdir(file_data)

c = 0       # for count

for i in file_data_list:
    file_path = file_data + '\\' + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
        
        print(data['data']['event_quantity'])
        c += data['data']['event_quantity']
        
print(c)        # 라이프 201, 부동산 790, 산업 6, 스포츠 71, 연예 8, 오피니언 4, 증권 1201