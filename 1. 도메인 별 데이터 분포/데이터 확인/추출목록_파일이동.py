# library
import pandas as pd
import os
import json
import shutil       # 파일 복사 및 이동


# 경로 설정
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_재전송_231123\\이벤트_통폐합\\trainning\\연예_E\\"    # 부동산, 스포츠, 오피니언, 증권, 라이프, 연예
result_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_재전송_231123\\이벤트_통폐합\\trainning\\E_result"       # 부동산, 스포츠, 오피니언, 증권, 라이프, 연예
path_file = os.listdir(path)
len(path_file)

# 추출 목록 할당
extract_list = [4138619,4137262, 4137239, 4137171, 4136046, 4133807, 4130882, 4128295, 4128232, 4128127, 4122852, 4122791, 4118310, 4118134, 4118093, 4117440, 4117103, 4111234, 4109184, 4106849 ] # 추출 목록 시 변경 필요
len(extract_list)


# JSON 내 변수값 할당
Da = 'Dataset'
Id = 'Identifier'


# 카운트용 변수 할당
c = 0
# 빈 리스트 생성
vin = []

# json 파일 호출
for i in path_file:
    json_path = path + "\\" + i
    with open(json_path, 'r', encoding='utf-8-sig')as file:
        data = json.load(file)
        
        # 조건 설정
        if data[Da][Id] in extract_list:
            print("Yes, it need extraction")
            print(data[Da]['name'])
            vin.append(data[Da]['name'])
            c += 1
            print(c)
            # 해당되는 json을 다른 경로로 추출
            
vin
len(vin)

# 조건문으로 path_file내에 있는 json 데이터를 result_path로 이동
for filename in vin:
    # 각 파일의 경로 설정
    source_file = os.path.join(path, filename)       
    destination_file = os.path.join(result_path, filename)

    # 파일 이동
    shutil.move(source_file, destination_file)
    print(f"{filename}을 {result_path}로 이동했습니다.")