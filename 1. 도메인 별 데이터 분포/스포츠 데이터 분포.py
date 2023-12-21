# library
import os
import json

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_S"       # 스포츠

file_list = os.listdir(path)

성적 = 0
기록 = 0
순위 = 0
수상 = 0
출전 = 0
대회 = 0
승부 = 0
경기결과 = 0
상금 = 0
계약 = 0
은퇴 = 0
cnt = 0

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_S\\" + i
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
            if event_idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:     # event_type KeyError
                cnt += 1
                event_type = data['data']['event'][event_idx]['event_argument'][0]['event_type']
            if event_type in ['성적']:
                성적 += 1
            elif event_type in ['기록']:
                기록 += 1
            elif event_type in ['순위']:
                순위 += 1
            elif event_type in ['수상']:
                수상 += 1
            elif event_type in ['출전']:
                출전 += 1
            elif event_type in ['대회']:
                대회 += 1
            elif event_type in ['승부']:
                승부 += 1
            elif event_type in ['경기결과']:
                경기결과 += 1
            elif event_type in ['상금']:
                상금 += 1
            elif event_type in ['계약']:
                계약 += 1      
            elif event_type in ['은퇴']:
                은퇴 += 1     

        data['data']['text_category_cd'] = "D-13-S"


print(성적)
print(기록)
print(순위)
print(수상)
print(출전)
print(대회)
print(승부)
print(경기결과)
print(상금)
print(계약)
print(은퇴)
print(cnt)