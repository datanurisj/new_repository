# library
import os
import json
import pandas as pd

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_O"       # 오피니언
file_list = os.listdir(path)

vin = []

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_O\\" + i
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
        data = data.replace('event_doc', 'sentence')
        data = eval(data)

        for event_idx in range(len(data['data']['event'])):
            if event_idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:  # 이벤트 인덱스가 0~10일 때
                event = data['data']['event'][event_idx]
                if 'event_argument' in event and len(event['event_argument']) == 1:
                    event_argument = event['event_argument']
                    event_type = event_argument[0]['event_type']
                    if event_type in ['주장']:    
                        event_type = '국내외 사건'
                    elif event_type in ['서술']:
                        event_type = '국내외 사건'
                    
                    event_argument[0]['event_type'] = event_type
                elif 'event_argument' in event and len(event['event_argument']) == 2:
                    event_argument = event['event_argument']
                    event_type = event_argument[0]['event_type']
                    if event_type in ['주장']:    
                        event_type = '국내외 사건'
                    elif event_type in ['서술']:
                        event_type = '국내외 사건'
                    event_argument[0]['event_type'] = event_type

                    event_type = event_argument[1]['event_type']
                    if event_type in ['주장']:    
                        event_type = '국내외 사건'
                    elif event_type in ['서술']:
                        event_type = '국내외 사건'
                    event_argument[1]['event_type'] = event_type

                elif 'event_argument' in event and len(event['event_argument']) == 3:
                    event_argument = event['event_argument']
                    event_type = event_argument[0]['event_type']
                    if event_type in ['주장']:    
                        event_type = '국내외 사건'
                    elif event_type in ['서술']:
                        event_type = '국내외 사건'
                    event_argument[0]['event_type'] = event_type

                    event_type = event_argument[1]['event_type']
                    if event_type in ['주장']:    
                        event_type = '국내외 사건'
                    elif event_type in ['서술']:
                        event_type = '국내외 사건'
                    event_argument[1]['event_type'] = event_type

                    event_type = event_argument[2]['event_type']
                    if event_type in ['주장']:    
                        event_type = '국내외 사건'
                    elif event_type in ['서술']:
                        event_type = '국내외 사건'
                    event_argument[2]['event_type'] = event_type
                else:
                    print(f"이벤트 {event_idx}에 대한 event_argument가 없거나 비어 있습니다.")
            else:
                print(f"이벤트 {event_idx}는 처리하지 않습니다.")

        data['data']['text_category_cd'] = "D-13-O"     # 오피니언
        

        save_path = 'C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206\\오피니언_O\\{}'.format(i)        # 오피니언
        with open(save_path, 'w', encoding='UTF8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


vin = list(vin)
df = pd.DataFrame()
df['list'] = vin

df.to_excel('오피니언_삭제목록.xlsx')