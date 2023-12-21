# library
import pandas as pd
import os
import json
import glob
import numpy as np

# path 
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\증권_T\\증권_1_test(334)\\"            # 수정 필요
path_file = glob.glob(path + "*.json")
len(path_file)

# vin list 생성
vin = []                            # 라이프, 부동산, 산업, 스포츠, 연예, 오피니언, 증권

# 변수 할당
d = 'Dataset'
id = 'Identifier'

for i in path_file:
    with open(i, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
        
        vin.append(data[d][id])
        
print(vin)

# list to excel
df = pd.DataFrame(vin)
df.to_excel('증권_Test_10%_고유값목록.xlsx')                     # 수정 필요          Test, Validation, Trainning

print(df)