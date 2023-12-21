import json
import os.path

def change_key(dict, old_key, new_key, point):
    print(dict.keys())
    dict[new_key] = dict.pop(old_key)
    keys = list(dict.keys())
    for j in range(point, len(keys) - 1):
        value = dict.pop(keys[j])
        dict[keys[j]] = value
        
    print(dict.keys())
    return dict

# 루트 및 변수 설정
Day = "이벤트_통폐합"
root = "C:\\Users\\user\\Downloads\\" + str(Day) + "\\home\\13-2MEE\\" # 트레이닝 디렉토리 루트 ~\\202310~
file_list = os.listdir(root) # 각 도메인별 디렉토리 루트

# event_doc -> sentence
for i in file_list:
    fl = os.listdir(root + i) # 각 도메인별 json파일들 저장
    for j in fl:
        file_path = root + i + "\\" + j
        with open (file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        for k in range(len(data['data']['event'])):
            if list(data['data']['event'][k].keys())[0] != "sentence":
                string = list(data["data"]["event"][k].keys())[0]
                data["data"]["event"][k] = change_key(data["data"]["event"][k], string, "sentence", 0)
        with open (file_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
