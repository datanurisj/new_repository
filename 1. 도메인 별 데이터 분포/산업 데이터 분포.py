# library
import os
import json

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_I"       # 산업
file_list = os.listdir(path)

합작 = 0
발전 = 0
개발 = 0
전략 = 0
계약 = 0
선택 = 0
매매 = 0
투자 = 0
수익 = 0
공개 = 0
기록 = 0
검증 = 0
실시 = 0
cnt = 0

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_I\\" + i
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
            if event_type in ['합작']:
                합작 += 1
            elif event_type in ['발전']:
                발전 += 1
            elif event_type in ['개발']:
                개발 += 1
            elif event_type in ['전략']:
                전략 += 1
            elif event_type in ['계약']:
                계약 += 1
            elif event_type in ['선택']:
                선택 += 1
            elif event_type in ['매매']:
                매매 += 1
            elif event_type in ['투자']:
                투자 += 1
            elif event_type in ['수익']:
                수익 += 1
            elif event_type in ['공개']:
                공개 += 1
            elif event_type in ['기록']:
                기록 += 1
            elif event_type in ['검증']:
                검증 += 1
            elif event_type in ['실시']:
                실시 += 1

        data['data']['text_category_cd'] = "D-13-I"


print(합작)
print(발전)
print(개발)
print(전략)
print(계약)
print(선택)
print(매매)
print(투자)
print(수익)
print(공개)
print(기록)
print(검증)
print(실시)
print(cnt)