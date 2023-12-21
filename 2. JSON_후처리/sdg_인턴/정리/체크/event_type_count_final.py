import json
import csv
import os.path
import pandas as pd
import copy

# 루트 및 변수 설정
Day = "이벤트_통폐합" # 루트설정용(없어도 됨)
# root = "C:\\Users\\user\\Downloads\\" + str(Day) + "\\" + "\\home\\13-2MEE\\" # 트레이닝 디렉토리 루트 ~\\202310~
root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\trainning\\"
#root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206_복사본\\trainning\\"
# csv_root = "C:\\Users\\user\\Downloads\\" + str(Day) +  "\\" + "\\home\\" # ***home 하위폴더(13-2MEE있는 위치)에 첨부한 csv_last, result폴더를 둘 것***
#csv_root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_1206_복사본\\"
csv_root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning\\"
file_list = os.listdir(root) # 각 도메인별 디렉토리 루트
e_count = 0
all_count = 0

# 개수 세기
for i in file_list:
    dom = i[len(i) - 1:] # E, I, L, O, R, S, T # 라이프_L폴더명의 L을 가져오는 형식, i[19:]는 툴로부터 다운 후 폴더의 경우
    DF = pd.read_csv(csv_root + "csv_last\\" + dom + ".csv") # csv_last폴더로부터 csv 호출
    fl = os.listdir(root + i) # 각 도메인별 json파일들 저장
    f = open(csv_root + "result\\" + dom + "_list.csv", 'w', newline="") # result폴더에 csv 작성
    wr = csv.writer(f)
    wr.writerow(["유형", "작업건수"])
    count = [0 for j in range(len(DF))]
    dom_count = 0
    for j in fl:
        dom_count = 0
        file_path = root + "\\" + i + "\\" + j
        with open (file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        eq = data['data']['event_quantity']
        if eq < 2: # event_quantity가 2개 미만일 경우를 체크
            with open(csv_root + "result\\" + str(Day) + "_eq_error.txt", 'a', newline="") as error:
                error.write(str(j) + "\n")
                e_count += 1
            print("eq에러 " + str(j))            
        try: # 키값의 오류가 없는 경우
            for k in data['data']['event']:                    
                for z in k['event_argument']:
                    error = copy.deepcopy(count)
                    for t in range(len(count)):
                        if z['event_type'] == DF['단어'].loc[t]:
                            count[t] += 1
                    if error == count: # 도메인별 모든 유형에 포함되지 않는 유형이 존재할 경우
                        with open(csv_root + "result\\" + str(Day) + "_notype_error.txt", 'a', newline="") as error:
                            error.write(str(j) + "\n")
                            e_count += 1
                            print(str(j))
        except: # 키값 손실 등의 이유로 위 코드가 실행되지 않은 경우
            with open(csv_root + "result\\" + str(Day) + "_all_error.txt", 'a', newline="") as error:
                error.write(str(j) + "\n")
                e_count += 1
                print(str(j))
    for k in range(len(count)):
        wr.writerow([DF['단어'].loc[k], count[k]])
        dom_count += count[k]
    wr.writerow(["총 검수량", dom_count])
    print("{dom} = {count}".format(dom = dom, count = count))
    print("카테고리 별 건수 : " + str(dom_count))
    all_count += dom_count
    f.close()

# 전체 이벤트 건수, 오류량 건수, 실제 이벤트 건 수 출력
print(all_count)
print(e_count)
print("End")