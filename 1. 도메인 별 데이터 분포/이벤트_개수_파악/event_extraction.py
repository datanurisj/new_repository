# library import 
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import csv
import re

# 함수 정의
def list_to_csv(data, filename):    # list to csv 저장
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def remove_parentheses(text):       # 괄호 제거 함수 정의
    return text.replace('[', '').replace(']', '')

def remove_quotes(text):            # 작은따옴표 제거 함수 
    return text.replace('\'','')

def remove_comma(text):
    return text.replace(',','')     # , 제거


# Path
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\KDX_Data_230813\\AI_HUB_13_O_2.csv"
csv = pd.read_csv(path, encoding = 'UTF8')

# copy
data = csv.copy()

# data 원하는 열 추출
#data1 = data[['IDX', 'ID', 'DATA_TITLE', 'DATA_TEXT', 'FILENAME', 'MEDIA_TYPE', 'MEDIA_NAME', 'CATEGORY', 'PUBDATE']]
data2 = data[['DATA_TEXT', 'PUBDATE']]

#data2.loc[data2['DATA_TEXT']]
ir = data2.DATA_TEXT    # interest_rates = 이자율 = 금리
       
pattern = r"(.*규제.*?)[\\\n\?\!]"  # '규제'와 '\n'을 기준으로 문장 추출
some = []

for i in ir:
    some.append(re.findall(pattern, i))     # '규제' 기준으로 문장 찾기

some = list(filter(None, some))     # 공백 제거

# 빈 데이터프레임 생성
df = pd.DataFrame()   
df['TEXT'] = some

# apply 함수를 사용해 열에 적용
df['TEXT'] = df['TEXT'].astype(str)                 # list to str
df['TEXT'] = df['TEXT'].apply(remove_parentheses)   # [] 제거
df['TEXT'] = df['TEXT'].apply(remove_quotes)        # '' 제거
df['TEXT'] = df['TEXT'].apply(remove_comma)         # ,  제거

# df 추출
#df.to_csv("C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\오피니언_규제_빈도문장.csv", encoding = 'cp949', index=False)


''' yjjo '''    # 문장 단위 추출
some2 = list()
for i in ir:
    some2 += [s for s in i.split('\n') if '규제' in s]

df2 = pd.DataFrame()
df2['TEXT'] = some2
df2.to_csv("C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\오피니언_규제_문장단위.csv", encoding = 'cp949')