import json
import csv
import os.path
import pandas as pd
import copy

# 루트 설정
root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_231121\\trainning\\"     # 부동산_R, 라이프_L, 증권_T, 스포츠_S
csv_root = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합_231121\\"

# 도메인 별 디렉토리 루트
file_list = os.listdir(root)

error_count = 0     # 에러 카운트
all_count = 0       # 전체 카운트

# 모든 파일별 이벤트 개수 확인
for i in file_list:             #   해당 디렉토리 접속
    document = i[len(i) - 1:]        #   마지막 영어 대문자 호출 : L, R, S, T 
    csv_last = pd.read_csv(csv_root + "csv_last\\" + document + ".csv")      # csv_last폴더에서 csv 호출
    fl = os.listdir(root + i)       # 도메인 별 json 파일 저장
    # result 폴더에 csv 작성
    f = open(csv_root + "result\\" + document + "_list.csv", 'w', newline="")    
    wr = csv.writer(f)
    wr.writerow(["이벤트 유형", "해당 작업 건수"])      # csv에 컬럼 작성
    count = [0 for _ in range(len(csv_last))]         # csv_last의 수만큼 0 생성
    dom_count = 0               # 문서 개수
    for j in fl:
        dom_count = 0
        file_path = root + i + "\\" + j             # R, L, S, T 디렉토리 입장 후 json 호출
        with open (file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        eq_count = data['data']['event_quantity']       # event_quantiy 값 할당
        if eq_count < 2:        # 이벤트 개수가 1개인것들을 찾아냄
            with open(csv_root + "result\\" + i + "이벤트_통폐합" + "_eq_count_error.txt", 'a', newline="")as error:
                error.write(str(j) + "\n")      # 파일 이름 + 줄바꿈
                error_count += 1
            print("eq_count에러" + str(j))
        try:        # data에서 실행 -> 이벤트 개수가 2개 이상인 것들
            for k in data['data']['event']:         # event 호출
                for z in k['event_argument']:       # event_argument 호출
                    error = copy.deepcopy(count)    # error 변수에 값 할당
                    for t in range(len(count)):     # count 개수만큼 반복
                        # event_type이 csv_last 단어 컬럼의 내용과 동일하면
                        if z['event_type'] == csv_last['단어'].loc[t]:     
                            count[t] += 1
                    if error == count:      # 도메인별 이벤트 유형에 포함되지 않는 경우
                        with open(csv_root + "result\\" + i + "_nonetype_error.txt", 'a', newline="") as e:
                            e.write(str(j) + "\n")
                            error_count += 1
                            print(str(j))
        except: # 그밖의 에러로 코드가 실행되지 않을때
            with open(csv_root + "result\\" + i + "_all_error.txt", 'a', newline="")as error:
                error.write(str(j) + "\n")
                error_count += 1
                print(str(j))
        for k in range(len(count)):             # 카운트의 개수만큼 반복
            wr.writerow([csv_last['단어'].loc[k], count[k]])        # ???
            dom_count += count[k]