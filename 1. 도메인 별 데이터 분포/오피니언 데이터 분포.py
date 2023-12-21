# library
import os
import json

# path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_O"       # 오피니언

file_list = os.listdir(path)

주장 = 0
서술 = 0
cnt = 0

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
        data = eval(data)

        for event_idx in range(len(data['data']['event'])):
            if event_idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:     # event_type KeyError
                cnt += 1
                event_type = data['data']['event'][event_idx]['event_argument'][0]['event_type']
            if event_type in ['주장']:
                주장 += 1
            elif event_type in ['서술']:
                서술 += 1
           
        data['data']['text_category_cd'] = "D-13-O"


print(주장)
print(서술)
print(cnt)