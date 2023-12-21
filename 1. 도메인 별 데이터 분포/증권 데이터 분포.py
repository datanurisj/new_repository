# library
import os
import json

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_T"       # 증권

file_list = os.listdir(path)

매매 = 0
보유 = 0
투자 = 0
상장 = 0
유지 = 0
거래 = 0
상승 = 0
하락 = 0
인수 = 0
자본 = 0
수익 = 0
기록 = 0
cnt = 0


for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_T\\" + i
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
            if event_idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                cnt += 1
                event_type = data['data']['event'][event_idx]['event_argument'][0]['event_type']
            if event_type in ['매매']:
                매매 += 1
            elif event_type in ['보유']:
                보유 += 1
            elif event_type in ['투자']:
                투자 += 1
            elif event_type in ['상장']:
                상장 += 1
            elif event_type in ['유지']:
                유지 += 1
            elif event_type in ['거래']:
                거래 += 1
            elif event_type in ['상승']:
                상승 += 1
            elif event_type in ['하락']:
                하락 += 1
            elif event_type in ['인수']:
                인수 += 1
            elif event_type in ['자본']:
                자본 += 1
            elif event_type in ['수익']:
                수익 += 1
            elif event_type in ['기록']:
                기록 += 1
            
        data['data']['text_category_cd'] = "D-13-T"


print(매매)
print(보유)
print(투자)
print(상장)
print(유지)
print(거래)
print(상승)
print(하락)
print(인수)
print(자본)
print(수익)
print(기록)
print(cnt)