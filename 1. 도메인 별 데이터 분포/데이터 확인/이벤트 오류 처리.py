# library
import os
import json
import pandas as pd
import numpy as np

# 데이터 경로
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1205\\라이프_L\\"       # 증권_T, 스포츠_S, 부동산_R, 라이프_L, 오피니언_O, 연예_E, 증권_T
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_재전송_231123\\이벤트_통폐합\\trainning\\증권_T\\"       # 증권_T, 스포츠_S, 부동산_R, 라이프_L
file_list = os.listdir(path)

# 중복되는 값 확인
# 변수 할당
x = 'data'
y = 'event'
z = 'event_entity'
b = 'event_argument'

# 중복값 발생 시 리스트 출력
duplicate_list = []

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1205\\라이프_L\\" + i       # 증권_T, 스포츠_S, 부동산_R, 라이프_L
    #file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_재전송_231123\\이벤트_통폐합\\trainning\\증권_T\\" + i       # 증권_T, 스포츠_S, 부동산_R, 라이프_L
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

        print()
        # event - event_entity - entity_value와  event - event_argument - trigger_value 가 동일한가?
        # 기본형 : entity_value 2개 , trigger_value 1개 case /// trigger_value가 n개 이상 case
        for i in range(len(data[x][y][0][z])):
            for l in range(len(data[x][y][0][b])):
                if data[x][y][0][z][i]['entity_value'] == data[x][y][0][b][l]['trigger_value']:
                    print("중복값 발생 확인됨")
                    duplicate_list.append(data['Dataset']['name'])
                else:
                    print("문제없음")

print(duplicate_list)

# 기타 에러 발생 시 리스트 출력
error_list = []

for i in file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1205\\라이프_L\\" + i
    #file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_재전송_231123\\이벤트_통폐합\\trainning\\증권_T\\" + i  # 해당 카테고리 작성
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data[x]['event_quantity'] >= 11:
            print("event_quantity Error 발생")
            print(data['Dataset']['Identifier'])
            error_list.append(data[x]['doc_id'])
            print(data[x]['event_quantity'])

        elif data[x][y][0]['event_argument'][0]['event_num'] >= 11:
            print("유효범위 오류 Error 발생")
            error_list.append(data[x]['doc_id'])
            print(data['Dataset']['Identifier'])
            print(data[x][y][0][b][0]['event_num'])

        elif data[x][y][0][b][0]['event_type'] == None:
            print("이벤트 타입 None 오류")
            error_list.append(data[x]['doc_id'])        # IDX 값
            print(data['Dataset']['Identifier'])        # ID 값
            print(data[x][y][0][b][0]['event_type'])

        elif data[x][y] == None:
            print('이벤트 이벤트 오류')
            error_list.append(data[x]['doc_id'])
            print(data['Dataset']['Identifier'])        

        elif data[x][y][0][b][0]['event_type'] == '기록':
            print('이벤트 유형 오류')
            error_list.append(data[x]['doc_id'])
            print(data['Dataset']['Identifer'])
        
        else:
            print("문제없음")
            
print(error_list)

        # for event_idx in range(len(data['data']['event'])):
        #     if event_idx in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:     # event_type KeyError
        #         cnt += 1
        #         event_type = data['data']['event'][event_idx][b][0]['event_type']
        #     if event_type in ['합작']:
        #         합작 += 1
        #     elif event_type in ['발전']:
        #         발전 += 1

