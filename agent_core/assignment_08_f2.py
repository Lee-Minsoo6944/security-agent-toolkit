import json

# 주어진 로그 데이터 (리스트 안에 딕셔너리가 들어 있는 구조)
logs = [{"user": "kim01", "count": 4}, {"user": "lee02", "count": 1}]

# 1. logs.json 파일에 데이터 저장하기 (직렬화)
with open("logs.json", "w", encoding="utf-8") as f:
  json.dump(logs, f, ensure_ascii=False, indent=2)

# 2. logs.json 파일에서 데이터 다시 읽어오기 (역직렬화)
with open("logs.json", "r", encoding="utf-8") as f:
  loaded_logs = json.load(f)

# 3. 첫 번째 기록의 user를 꺼내어 출력하기 (결과: kim01)
print(logs[0]["user"])