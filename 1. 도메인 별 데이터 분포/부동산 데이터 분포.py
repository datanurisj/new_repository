# library
import os
import json

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_R"       # 부동산
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_1\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_R"
file_list = os.listdir(path)

시장분석 = 0
사업 = 0
기록 = 0
검증 = 0
처분 = 0
피해 = 0
매매 = 0
투자 = 0
신청 = 0
계약 = 0
정책 = 0
임명 = 0
cnt = 0

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_R\\" + i
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
            if event_type in ['시장분석']:
                시장분석 += 1
            elif event_type in ['사업']:
                사업 += 1
            elif event_type in ['기록']:
                기록 += 1
            elif event_type in ['검증']:
                검증 += 1
            elif event_type in ['처분']:
                처분 += 1
            elif event_type in ['피해']:
                피해 += 1
            elif event_type in ['매매']:
                매매 += 1
            elif event_type in ['투자']:
                투자 += 1
            elif event_type in ['신청']:
                신청 += 1
            elif event_type in ['계약']:
                계약 += 1      
            elif event_type in ['정책']:
                정책 += 1
            elif event_type in ['임명']:
                임명 += 1     
            #else:
            #    시장분석 += 1
        data['data']['text_category_cd'] = "D-13-R"


print(시장분석)
print(사업)
print(기록)
print(검증)
print(처분)
print(피해)
print(매매)
print(투자)
print(신청)
print(계약)
print(정책)
print(임명)
print(cnt)