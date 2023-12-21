# library
import json
import pandas as pd
from tqdm import tqdm
from time import sleep
import glob
import os

# 전처리할 디렉토리 경로
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\회사\\3. 2023 사업\\4. AI 학습용데이터\\01. 한국어_다중이벤트\\13.1 데이터\\1. JSON 데이터\\final\\이벤트_354건_후처리_231206\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_I\\"       # 산업
file_list = glob.glob(path + "*.json")  # path내 json파일 호출

# len
len(file_list)      # I 데이터 목록 969

# 필요없는 유형 목록 담기
vin = []

# 이벤트 목록 사전 구조 작성
event_type = {'산업제품의 안전점검' : '검증',
              '산업제품 매매' : '매매',
              '산업제품출시' : ['공개', '실시'],
              '산업업체의 발전' : ['합작', '발전', '개발', '전략', '기록', '계약', '투자'],
              '산업업체의 수익' : '수익'}

# 변수값 할당
d = 'data'
e = 'event'
er = 'event_argument'


for i in tqdm(file_list):
    with open(i, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
        
        data = str(data)        # str
        # 데이터 값 변경
        data = data.replace('document', 'data')
        data = data.replace('document_text', 'data')
        data = data.replace('data_text', 'data')
        data = data.replace('Entity_value', 'entity_value')
        data = data.replace('identifier', 'Identifier')
        data = data.replace('news_category', 'text_category')
        data = data.replace('news_cateogry_cd', 'text_category_cd')
        data = data.replace('MEE_Training', 'MEE_Trainning')
        data = data.replace('event_doc', 'sentence')    # sentence 변경
        data = data.replace('\\n', '')                   # \n값 삭제      
        data = data.replace('\\u0027', '\'')            # 유니코드 \u0027 변경  
             
        data = eval(data)           # str -> dict
        
        data[d]['text_category_cd'] = "D-13-I"      # 카테고리 이름 D_13_I -> D-13-I로 변경
        
        for j in range(len(data[d][e])):                            # data['data']['event'] 개수
            for k in range(len(data[d][e][j][er])):                             # j['event_argument']
                if data[d][e][j][er][k]["event_type"] in event_type['산업제품의 안전점검']:     # 산·안 value 값 존재
                    data[d][e][j][er][k]["event_type"] = '산업제품의 안전점검'
                elif data[d][e][j][er][k]["event_type"] in event_type['산업제품 매매']:         # 산·매 value값 존재
                    data[d][e][j][er][k]["event_type"] = '산업제품 매매'
                elif data[d][e][j][er][k]["event_type"] in event_type['산업제품출시']:       # 산업제품출시 value값 존재
                    data[d][e][j][er][k]["event_type"] = '산업제품출시'
                elif data[d][e][j][er][k]["event_type"] in event_type['산업업체의 발전']:     # 산·발 value 값 존재
                    data[d][e][j][er][k]["event_type"] = '산업업체의 발전'
                elif data[d][e][j][er][k]["event_type"] in event_type['산업업체의 수익']:       # 산·수 value 값 존재
                    data[d][e][j][er][k]["event_type"] = '산업업체의 수익'
                else:           # 그 외의 '선택' 등의 데이터
                    vin.append(data['Dataset']['name'])
                    # print(data['Dataset']['name'])
        
        # 저장
        save_path = 'C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_테스트파일\\산업_I\\{}'.format(i[166:198])
        with open(save_path, 'w', encoding='UTF8')as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        #sleep(0.1)
        #break



# 이벤트 1개 데이터 확인
f_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_테스트파일\\산업_I\\"
industry_list = os.listdir(f_path)       # 파일 경로내 데이터 목록 출력

# idx, event_quantity 담을 빈 목록 생성
i_name_list = []

for i in tqdm(industry_list):
    industry_file_path = f_path + i         # 산업 경로
    with open(industry_file_path, 'r', encoding='utf-8-sig')as file:
        data = json.load(file)
        
        if data[d]['event_quantity'] == 1:          # 이벤트 개수 1개인것 확인
            i_name_list.append(data['Dataset']['name'])
            


# 리스트에 데이터 추가  
# 데이터가 2개, l_name_list 안에 데이터가 있으면 하나씩 vin에 추가
# 이벤트 개수가 1개인 데이터가 없음
len(vin)
for i in range(len(i_name_list)):
    if i_name_list is not None: 
        vin.append(i_name_list[i])
    else:
        print("예외 발생, 확인 필요")
len(vin)


# vin의 데이터 목록 제거
vin = set(vin)              # 중복 제거
count = 0                   # 카운트 용


# f_path 경로 재사용
for name in vin:
    file_path = os.path.join(f_path, name)
    if name in industry_list:        # 중복데이터가 데이터 목록 내 존재한다면
        os.remove(file_path)        # 해당 데이터 삭제
        print(f'{name} 중복 파일 삭제 완료')
        count += 1
        print(count)
    else:
        print(f'{name} 해당 파일을 찾을 수 없음')
        
vin = list(vin)
df = pd.DataFrame()     # 빈 df 생성
df['list'] = vin        # df에 vin 집어 넣기

# 저장경로 설정(엑셀로 저장)
df.to_excel("C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_테스트파일\\산업_삭제목록.xlsx")     




# \n값, \u0027 데이터 확인
check_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\한국어_테스트파일\\산업_I\\*"
json_file = glob.glob(f'{check_path}.json')

vin2_n = []
vin2_uni = []

for name in tqdm(json_file):
    with open(name, 'r', encoding='UTF-8')as f:
        data_str = f.read()
        
        if '\\n' in data_str:
            print(f'The File {name} is still survived \\n')
            vin2_n.append(name)
        elif '\\u0027' in data_str:
            print(f'The File {name} is still survived \\u0027')
            vin2_uni.append(name)
        else:
            continue
            
print(vin2_n)
print(vin2_uni)
