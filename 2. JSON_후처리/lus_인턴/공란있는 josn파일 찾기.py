import os
import json
import pandas as pd

vin = []

def find_json_files_with_spaces_in_trigger_value(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if 'data' in data and 'event' in data['data']:
                        events = data['data']['event']
                        for event in events:
                            if 'event_argument' in event:
                                arguments = event['event_argument']
                                for argument in arguments:
                                    if argument['trigger_value'].startswith(' ') or argument['trigger_value'].endswith(' '):
                                        print(f"JSON file with spaces around trigger value: {file}")
                                        vin.append(file)
# 폴더 경로를 지정
find_json_files_with_spaces_in_trigger_value("C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_T")

df = pd.DataFrame()
df['list'] = vin

df.to_excel('증권_공란json_리스트.xlsx') 
print("없습니다.")