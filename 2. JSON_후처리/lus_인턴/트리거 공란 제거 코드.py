import os
import re

# 폴더 경로 설정
folder_path = "C:\\Users\\이성재\\OneDrive - 데이터누리\\바탕 화면\\이벤트_통폐합\\라이프_L\\"      # 라이프, 부동산, 산업, 스포츠, 연예, 오피니언, 증권

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
            content = f.read()

        # trigger_value 값을 찾아 앞뒤 공백 제거
        pattern = r'("trigger_value": ")(.*?)(")'
        replacement = lambda match: match.group(1) + match.group(2).strip() + match.group(3)
        content = re.sub(pattern, replacement, content)

        # 수정된 내용을 원본 파일에 다시 쓰기
        with open(os.path.join(folder_path, filename), 'w', encoding='utf-8') as f:
            f.write(content)
