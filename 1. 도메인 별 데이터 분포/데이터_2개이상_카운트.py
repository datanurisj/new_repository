import os
import json

# 증권 path
t_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_T"       # 증권
t_file_list = os.listdir(t_path)

t_idx_list = []
t_qty_list = []

for i in t_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_T\\" + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            t_idx_list.append(data['Dataset']['Identifier'])
            t_qty_list.append(data['data']['event_quantity'])

# 라이프 path
#l_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_L"       # 라이프
l_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1205\\라이프_L"
l_file_list = os.listdir(l_path)

l_idx_list = []
l_qty_list = []

for i in l_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_L\\" + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            l_idx_list.append(data['Dataset']['Identifier'])
            l_qty_list.append(data['data']['event_quantity'])


# 부동산 path
r_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_R"       # 부동산
r_file_list = os.listdir(r_path)

r_idx_list = []
r_qty_list = []

for i in r_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_R\\" + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            r_idx_list.append(data['Dataset']['Identifier'])
            r_qty_list.append(data['data']['event_quantity'])


# 산업 path
i_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_I"       # 산업
i_file_list = os.listdir(i_path)

i_idx_list = []
i_qty_list = []

for i in i_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_I\\" + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            i_idx_list.append(data['Dataset']['Identifier'])
            i_qty_list.append(data['data']['event_quantity'])


# 스포츠 path
s_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_S"       # 스포츠
s_file_list = os.listdir(s_path)

s_idx_list = []
s_qty_list = []

for i in s_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_S\\" + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            s_idx_list.append(data['Dataset']['Identifier'])
            s_qty_list.append(data['data']['event_quantity'])


# 연예 path
e_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_E"       # 연예
e_file_list = os.listdir(e_path)

e_idx_list = []
e_qty_list = []

for i in e_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_E\\" + i 
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            e_idx_list.append(data['Dataset']['Identifier'])
            e_qty_list.append(data['data']['event_quantity'])


# 오피니언 path
o_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_O"       # 오피니언
o_file_list = os.listdir(o_path)

o_idx_list = []
o_qty_list = []

for i in o_file_list:
    file_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home_231020\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_O\\" + i
    with open (file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)

        if data['data']['event_quantity'] == 1:
            o_idx_list.append(data['Dataset']['Identifier'])
            o_qty_list.append(data['data']['event_quantity'])


len(t_idx_list)       # 증권
len(e_idx_list)       # 연예
len(s_idx_list)       # 스포츠
len(r_idx_list)       # 부동산
len(o_idx_list)       # 오피니언
len(i_idx_list)       # 산업
len(l_idx_list)       # 라이프
l_qty_list
sum(l_qty_list)

total = []
total = t_idx_list + e_idx_list + s_idx_list + r_idx_list + o_idx_list + i_idx_list + l_idx_list
len(total)              # 모든 카테고리 숫자

# 모든 event_quantity 합
print(sum(t_qty_list) + sum(e_qty_list) + sum(s_qty_list) + sum(r_qty_list) + sum(o_qty_list) + sum(i_qty_list) + sum(l_qty_list))