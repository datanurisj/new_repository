import json
import pandas as pd
import os.path

# 루트 및 변수 설정
Day = "이벤트_통폐합" # 루트설정용(없어도 됨)
#root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\01. 이벤트\\05. 이벤트 통폐합\\1. 통폐합_final\\이벤트_통폐합_final\\증권_T\\"   
root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206\\증권_T\\"                    # 라이프_L 1074, 부동산_R 1127, 산업_I 873, 연예_E 946, 오피니언_O 832, 증권_T 1379, 스포츠_S 1003 작업 필요.(231121)
#root = "C:\\Users\\user\\Downloads\\" + str(Day) + "\\home\\13-2MEE\\" # 트레이닝 디렉토리 루트 ~\\202310~
csv_root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206\\"
#csv_root = "C:\\Users\\user\\Downloads\\" + str(Day) + "\\home\\" # ***home 하위폴더(13-2MEE있는 위치)에 첨부한 result폴더를 둘 것***
file_list = os.listdir(root) # 각 도메인별 디렉토리 루트

# 공백 제거 및 value수정
for i in file_list:
    dom = i[len(i) - 1:] # E, I, L, O, R, S, T # 라이프_L폴더명의 L을 가져오는 형식, i[19:]는 툴로부터 다운 후 폴더의 경우
    fl = os.listdir(root)
    for j in fl:
        file_path = root + j
        with open (file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        try: # 키값의 오류가 없는 경우
            for k in range(len(data['data']['event'])):                                             # dd
                for z in range(len(data['data']['event'][k]['event_entity'])):
                    string = str(data['data']['event'][k]['event_entity'][z]['entity_value'])
                    if string.startswith(" "): # 앞 공백이 있는 경우
                        string = string[1:]                                                         # 공백 없애기
                        print(str(j))
                    if string.endswith(" "): # 뒷 공백이 있는 경우
                        string = string[:len(string) - 1]                                           # 공백 없애기
                        print(str(j))
                    data['data']['event'][k]['event_entity'][z]['entity_value'] = string            
                    data['data']['event'][k]['event_entity'][z]['entity_length'] = len(string)
                    data['data']['event'][k]['event_entity'][z]['start_index'] = data['data']['event'][k]['sentence'].find(string) # 걱정되는 부분은 해당 entity가 문장에서 2번 이상 반복될 경우 마지막 index를 가져옴
                    data['data']['event'][k]['event_entity'][z]['end_index'] = data['data']['event'][k]['event_entity'][z]['start_index'] + len(string)
                    with open (file_path, 'w', encoding="utf-8") as file:      
                        json.dump(data, file, ensure_ascii=False, indent=4)     # 데이터 덮어쓰기
                for z in range(len(data['data']['event'][k]['event_argument'])):
                    string = str(data['data']['event'][k]['event_argument'][z]['trigger_value'])
                    if string.startswith(" "):
                        string = string[1:]                                     # 공백 없애기
                        print(str(j))
                    if string.endswith(" "):
                        string = string[:len(string) - 1]                       # 공백 없애기
                        print(str(j))
                    data['data']['event'][k]['event_argument'][z]['trigger_value'] = string
                    data['data']['event'][k]['event_argument'][z]['trigger_length'] = len(string)
                    data['data']['event'][k]['event_argument'][z]['trigger_start_index'] = data['data']['event'][k]['sentence'].find(string) # 걱정되는 부분은 해당 tirgger가 문장에서 2번 이상 반복될 경우 마지막 index를 가져옴
                    data['data']['event'][k]['event_argument'][z]['trigger_end_index'] = data['data']['event'][k]['event_argument'][z]['trigger_start_index'] + len(string)
                    with open (file_path, 'w', encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)     # 데이터 덮어쓰기

        except Exception as e: # 키값 손실 등의 이유로 위 코드가 실행되지 않은 경우
            print(str(e))
            with open(csv_root + "result\\" + "remove_error.txt", 'a', newline="") as error:
                error.write(str(e) + " " + str(j) + "\n")
            print(str(j))
        # print("{dom}-{id} 작업완료".format(dom = dom, id = data['Dataset']['Identifier']))
    print(str(dom) + "완료")
    break

ex = "배우 박해일과 탕웨이"