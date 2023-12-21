# library
import os
import json
import pandas as pd
import numpy as np

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_E"       # 연예

file_list = os.listdir(path)

영화 = 0
관객 = 0
흥행 = 0
제작 = 0
작품 = 0
노래 = 0
공연 = 0
컴백 = 0
영상 = 0
차트 = 0
수상 = 0
데뷔 = 0
cnt = 0
idx_list = []

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_E\\" + i 
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        data = str(data)
        data = data.replace('document', 'data')
        data = data.replace('document_text', 'data')
        data = data.replace('data_text', 'data')
        data = data.replace('Entity_value', 'entity_value')
        data = data.replace('identifier', 'Identifier')
        data = data.replace('news_category', 'text_category')
        data = data.replace('news_cateogry_cd', 'text_category_cd')
        data = data.replace('MEE_Training', 'MEE_Trainning')
        data = eval(data)

        for event_idx in range(len(data['data']['event'])):
            event_argument = data['data']['event'][event_idx]['event_argument'][0]
    
            if 'event_type' in event_argument:
                event_type1 = event_argument['event_type']
                cnt += 1
                if event_type1 in ['영화']:
                    영화 += 1
                elif event_type1 in ['관객']:
                    관객 += 1
                elif event_type1 in ['흥행']:
                    흥행 += 1
                elif event_type1 in ['제작']:
                    제작 += 1
                    idx_list.append(data['data']['doc_id']) # 제작 idx 
                elif event_type1 in ['노래']:
                    노래 += 1
                elif event_type1 in ['공연']:
                    공연 += 1
                elif event_type1 in ['컴백']:
                    컴백 += 1
                elif event_type1 in ['영상']:
                    영상 += 1
                elif event_type1 in ['차트']:
                    차트 += 1
                elif event_type1 in ['수상']:
                    수상 += 1
                elif event_type1 in ['기록']:
                    데뷔 += 1
                else:
                     작품 += 1
            else:
                작품 += 1



print(영화)
print(관객)
print(흥행)
print(제작)
print(작품)
print(노래)
print(공연)
print(컴백)
print(영상)
print(차트)
print(수상)
print(데뷔)
print(cnt)



print(idx_list)
idx_list = set(idx_list)
idx_list = sorted(idx_list, reverse=False)
#idx_list = str(idx_list)

df = pd.DataFrame(idx_list)
df.to_excel('연예 제작 중복 idx값.xlsx')