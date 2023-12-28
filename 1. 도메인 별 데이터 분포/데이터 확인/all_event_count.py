# library
import json
import os


# 이벤트 개수 파악
path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\trainning분류_test_validation_231228_175삭제_통합\\trainning\\"        # trainning안에 라이프_L, 오피니언_O 만 존재해야함. 이하 생략..
folder_list = os.listdir(path)


# 카테고리별 사전
life = {'여행' : 0, '상품판매': 0, '국내업체의 기술개발' : 0, '공개' : 0, '질병' : 0}
entertainment = {'영화 정보' : 0, '가수 활동' : 0, '앨범 발매' : 0, '수상 정보' : 0, '음원 차트 순위' : 0}
industry = {'산업제품의 안전점검' : 0, '산업제품 매매' : 0, '산업제품출시' : 0, '산업업체의 발전' : 0, '산업업체의 수익' : 0}
opinion = {'국내외 사건' : 0}
sport = {'선수 성적' : 0, '선수 순위': 0, '경기 결과' : 0, '경기 승부 정보' : 0, '선수 거취' : 0}
transform = {'증권 영업이익' : 0, '증권 매매' : 0, '증권 거래 정보' : 0, '증권회사 인수' : 0, '증권분석' : 0}
real_estate = {'부동산 매매' : 0, '부동산 시장분석' : 0, '부동산 정책' : 0, '건축건설 사업' : 0, '부동산 피해' : 0}

vin = []


# 변수 할당
d = 'data'
e = 'event'
eq = 'event_quantity'
ea = 'event_argument'
et = 'event_type'


# 전체 이벤트 개수 파악
for folder in folder_list:
    folder_path = os.path.join(path, folder)
    files_in_folder = os.listdir(folder_path)
    for file_name in files_in_folder:
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.json'):     # JSON 파일 읽기
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
                for i in range(len(data[d][e])):
                    for j in range(len(data[d][e][i][ea])):
                        event_type = data[d][e][i][ea][j][et]
                        # 각 카테고리별 event_type 카운트
                        if event_type in life:
                            life[event_type] += 1
                        elif event_type in entertainment:
                            entertainment[event_type] += 1
                        elif event_type in industry:
                            industry[event_type] += 1
                        elif event_type in opinion:
                            opinion[event_type] += 1
                        elif event_type in sport:
                            sport[event_type] += 1
                        elif event_type in transform:
                            transform[event_type] += 1
                        elif event_type in real_estate:
                            real_estate[event_type] += 1
                        else:
                            vin.append(event_type)



# 결과 확인                            
print("라이프 카테고리:", life, "라이프 총 합:", sum(life.values()))
print("연예 카테고리:", entertainment, "연예 총 합:", sum(entertainment.values()))
print("산업 카테고리:", industry, "산업 총 합:", sum(industry.values()))
print("오피니언 카테고리:", opinion, "오피니언 총 합:", sum(opinion.values()))
print("스포츠 카테고리:", sport, "스포츠 총 합:", sum(sport.values()))
print("증권 카테고리:", transform, "증권 총 합:", sum(transform.values()))
print("부동산 카테고리:", real_estate, "부동산 총 합:", sum(real_estate.values()))

# 전체 총 합
print(sum(life.values()) + sum(entertainment.values()) + sum(industry.values()) + sum(opinion.values()) + sum(sport.values()) + sum(transform.values()) + sum(real_estate.values()))
