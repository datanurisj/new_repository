import json
import glob
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# 폴더 내 모든 JSON 파일 읽기 & 텍스트 추출 
file_list = glob.glob('C:\\Users\\이우성\\Desktop\\home\\13-2MEE\\MEE_Trainning\\MEE_Trainning_D_13_E\\*.json')  # 경로 수정 필요 
texts = []
for file in file_list:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        texts.append(data['data']['text'])

# 유사도 계산 - TF-IDF & 코사인 유사도 사용 
tfidf = TfidfVectorizer().fit_transform(texts)
cosine_similarities = cosine_similarity(tfidf[0:], tfidf)

results = {}

for idx, row in enumerate(cosine_similarities):
    similar_indices = row.argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], file_list[i]) for i in similar_indices]

    results[file_list[idx]] = similar_items[1:]

def item(id):
    return texts[file_list.index(id)]

# 가장 비슷한 문서와 그 문서의 similarity 점수 반환 함수 
def recommend(item_id, num):
    recs = results[item_id][:num]
    return recs

# 결과 저장 - 엑셀에 저장하기 위해 DataFrame 생성 후 to_excel 함수 사용  
df=pd.DataFrame(columns=['Source File','Similar File','Similarity Score'])

for source_file in file_list:
   rec=recommend(source_file,1)[0]  # 각 파일마다 가장 비슷한 하나의 파일만 추천받음.
   similarity_score=round(rec[0]*100, 1) # 소수점 첫째자리까지의 백분율로 나타냄.
   
   if similarity_score >= 80: # Similarity Score가 80 이상일 때만 DataFrame에 추가.
       temp_df=pd.DataFrame({'Source File':[os.path.basename(source_file)],'Similar File':[os.path.basename(rec[1])],'Similarity Score':[similarity_score]})
       df=pd.concat([df,temp_df],ignore_index=True)


df.to_excel('C:\\Users\\이우성\\Desktop\\home\\new\\similarities.xlsx')
