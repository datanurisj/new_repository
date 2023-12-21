import json
import csv
import os.path
import pandas as pd

# 루트 및 변수 설정
root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\13-2MEE\\MEE_Trainning\\" # 트레이닝 디렉토리 루트 ~\\202310~
# csv_root = "C:\\Users\\user\\Desktop\\20231011085634\\home\\" # ***home 하위폴더(13-2MEE있는 위치)에 첨부한 csv, result폴더를 둘 것***
csv_root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\home\\"
file_list = os.listdir(root) # 각 도메인별 디렉토리 루트
all_count = 0 # 모든 오류없는 이벤트 건 수 합
all_e_count = 0 # 모든 오류 "파일" 건 수 합
real_event = 0 # event_quantity를 활용하여 센 실제 이벤트 건수
# 오류 "이벤트" 건수 = real_event - all_count

# 개수 세기
for i in file_list:
    dom = i[19:] # E, I, L, O, R, S, T
    dom_count = 0
    e_count = 0
    DF = pd.read_csv(csv_root + "csv\\" + dom + ".csv") # csv폴더로부터 csv 호출
    fl = os.listdir(root + "\\" + i) # 각 도메인별 json파일들 저장
    f = open(csv_root + "result\\" + dom + "_list.csv", 'a', newline="") # result폴더에 csv 작성
    wr = csv.writer(f)
    for j in range(len(DF)):
        count = 0
        for k in fl:
            file_path = root + "\\" + i + "\\" + k
            with open (file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
            try: # 아래 코드에 오류가 없는 경우(이벤트 타입이 존재하는 경우)
                if j == 0:
                    real_event += int(data['data']['event_quantity'])
                for z in data['data']['event']:
                    for t in z['event_argument']:
                        if t['event_type'] == DF['단어'].loc[j]:
                            count += 1
                print(str(k) + " " + str(DF['단어'].loc[j]) + " " + str(count))
            except: # 오류 발생(이벤트 타입이 없는 경우)
                error = open(csv_root + "result\\" + "error.txt", 'a', newline="")
                error.write(str(k) + "\n")
                print(str(k))
                e_count += 1
        dom_count += count

        # csv내 단어, 이벤트 건 수 작성
        wr.writerow([DF['단어'].loc[j], count])
        print(str(DF['단어'].loc[j]) + " " + str(count))
    all_count += dom_count
    all_e_count += e_count
    # csv 파일 마지막에 전체검수량과 오류량 작성
    wr.writerow(["전체검수량", dom_count])
    wr.writerow(["오류량", e_count])
    f.close()

# 전체 이벤트 건수, 오류량 건수, 실제 이벤트 건 수 출력
print(all_count)
print(all_e_count)
print(real_event)
print("모두 작업완료")