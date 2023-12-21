import os
import json
import re
from tqdm import tqdm
from time import sleep
import glob

# path
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\라이프_L\\life_8"       # 라이프_L
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\부동산_R\\부동산_8"         # 부동산_R
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\산업_I\\산업_8"          # 산업_I
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\스포츠_S\\스포츠_8"          # 스포츠_S
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\연예_E\\연예_8"          # 연예_E
#path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\오피니언_O\\오피니언_8"          # 오피니언_O
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\증권_T\\증권_8"          # 증권_T
file_list = os.listdir(path)
len(file_list)

c = 0       # for count

for i in file_list:
    file_path = path + '\\' + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
        
        # print(data['data']['event_quantity'])
        c += data['data']['event_quantity']
        
print(c)        # print count




### 데이터 파일 이름 바꾸기
test_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\증권_T\\증권_1_validation(334)"         # 라이프, 부동산, 산업, 스포츠, 연예, 오피니언, 증권            # 수정
test_file_list = os.listdir(test_path)

for file in test_file_list:                 # 전체 파일 리스트에 대해 수행
    src = os.path.join(test_path, file)     # 기존 파일 경로
    dst_name = file.replace("Trainning", "Validation")        # 수정                  Test, Validation                                                                     # 수정
    dst = os.path.join(test_path, dst_name)        # 바뀐 이름 파일 경로
    os.rename(src, dst)                                 # rename 실행



### 데이터 내 데이터 바꾸기
test_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\증권_T\\증권_1_validation(334)\\"         # 라이프, 부동산, 산업, 스포츠, 연예, 오피니언, 증권            # 수정
test_file_list = glob.glob(test_path + "*.json")
len(test_file_list)

for i in test_file_list:
    with open(i, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)                         # json 형식의 데이터 호출
        
        data = str(data)                # str로 변경
        
        data = re.sub("[Tt]rainning", "Validation", data)     # re.sub로 Trainning -> Test로 변경               Test, Validation                                   # 수정
        
        data = eval(data)           # dict로 변경
        
        
        # save
        save_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\증권_T\\증권_1_Validation_334\\{}".format(i[82:120])            # 수정
        with open(save_path, 'w', encoding='utf-8-sig') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

