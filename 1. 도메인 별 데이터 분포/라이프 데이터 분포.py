# library
import os
import json

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_L"       # 라이프
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합\\라이프_L"
file_list = os.listdir(path)

질병 = 0
성장 = 0
발전 = 0
적용 = 0
수익 = 0
매매 = 0
개최 = 0
운영 = 0
물가 = 0
기록 = 0
공개 = 0
cnt = 0

vin =[]

# 사람 = 0
# 기업 = 0
# 이익 = 0
# 일상 = 0


for i in file_list:
    #file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합\\라이프_L\\" + i
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_L\\" + i
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
                # event_type2가 있는지 확인하고 카운트
                if 'event_argument' in data['data']['event'][event_idx] and len(data['data']['event'][event_idx]['event_argument']) >= 2:
                    event_type2 = data['data']['event'][event_idx]['event_argument'][1]['event_type']
                    cnt += 1
                    if event_type2 in ['질병']:
                        질병 += 1
                    elif event_type2 in ['성장']:
                        성장 += 1
                    elif event_type2 in ['발전']:
                        발전 += 1
                    elif event_type2 in ['적용']:
                        적용 += 1
                    elif event_type2 in ['수익']:
                        수익 += 1
                    elif event_type2 in ['매매']:
                        매매 += 1
                    elif event_type2 in ['개최']:
                        개최 += 1
                    elif event_type2 in ['운영']:
                        운영 += 1
                    elif event_type2 in ['물가']:
                        물가 += 1
                    elif event_type2 in ['기록']:
                        기록 += 1
                    elif event_type2 in ['공개']:
                        공개 += 1
                    else:
                        vin += 1
                else:
                    pass
                if event_type in ['질병']:
                    질병 += 1
                elif event_type in ['성장']:
                    성장 += 1
                elif event_type in ['발전']:
                    발전 += 1
                elif event_type in ['적용']:
                    적용 += 1
                elif event_type in ['수익']:
                    수익 += 1
                elif event_type in ['매매']:
                    매매 += 1
                elif event_type in ['개최']:
                    개최 += 1
                elif event_type in ['운영']:
                    운영 += 1
                elif event_type in ['물가']:
                    물가 += 1
                elif event_type in ['기록']:
                    기록 += 1
                elif event_type in ['공개']:
                    공개 += 1
                else:
                    vin += 1
            
            data['data']['text_category_cd'] = "D-13-L"

print(질병)
print(성장)
print(발전)
print(적용)
print(수익)
print(매매)
print(개최)
print(운영)
print(물가)
print(기록)
print(공개)
print(vin)
print(cnt)
