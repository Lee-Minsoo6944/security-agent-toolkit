# 줄 수를 세기 위한 상자(변수)를 0부터 시작하도록 준비합니다.
count = 0

# sample_logs.csv 파일을 읽기 모드로 엽니다.
with open("sample_logs.csv", encoding="utf-8") as f:
    for line in f:
        # strip()을 사용해 양쪽의 불필요한 빈 줄이나 공백을 제거하고 출력합니다.
        print(line.strip())
        
        # 줄을 하나 읽을 때마다 카운트 상자에 1씩 더해줍니다.
        count += 1

# 반복이 모두 끝난 후, 총 몇 줄인지 출력합니다.
print(f"총 {count}줄")