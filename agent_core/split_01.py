# 2.1 split 이 조용히 틀린다
line = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"
parts = line.split()
print(parts[6])      # kim01  ← 6번 칸이 계정이다

# 문제 2-1 · 무엇이 보일까요
# 내 예상 → kim.cs
line = "2026-09-29 09:02:11 INFO accepted login for kim.cs from 10.1.2.11"
parts = line.split()
print(parts[6])

# 문제 2-2 · 무엇이 보일까요
# 내 예상 → invalid (계정 guest 가 아니라 invalid 가 나온다, 에러는 없다)
line = "2026-09-29 23:40:07 WARN failed login for invalid user guest from 185.220.101.34"
parts = line.split()
print(parts[6])

# 문제 2-3 · 칸 개수 세기 (나와야 하는 결과: 9 · 11)
line1 = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"
line2 = "2026-09-29 23:40:07 WARN failed login for invalid user guest from 185.220.101.34"

parts = line1.split()     # 빈칸으로 자를 때는 split() 안에 아무것도 넣지 않는다
print(len(parts))         # len() 으로 리스트 개수를 센다

parts = line2.split()
print(len(parts))

# 문제 2-5 · 파일 전체에서 6번 칸 보기
# 이 코드에서 하는 일: 파일의 각 줄에서 6번 칸을 확인한다
# 왜 하나: 줄마다 같은 자리에 원하는 값이 있는지 살펴본다
print("---- 문제 2-5 ----")

# 1. 로그 파일을 연다
with open("raw_logs.txt", "r", encoding="utf-8") as f:
    # 2. 파일을 한 줄씩 반복한다
    for line in f:
        # 3. 현재 줄을 빈칸으로 나누고 6번 칸을 출력한다
        parts = line.split()
        print(parts[6])

# 도전 2-6 · 번호가 밀린 줄을 찾아내기
# 이 코드에서 하는 일: 빈칸으로 자른 값의 개수가 9 가 아닌 줄을 통째로 출력한다
# 왜 하나: 문제 2-5에서 6번 값이 계정이 아니었던 줄을 골라낸다
print("---- 도전 2-6 ----")

# 1. 로그 파일을 연다
with open("raw_logs.txt", "r", encoding="utf-8") as f:
    # 2. 파일을 한 줄씩 반복한다
    for line in f:
        # 3. 현재 줄을 빈칸으로 나눈다
        parts = line.split()
        # 4. 값의 개수가 9 가 아니면 (!= 는 같지 않다)
        if len(parts) != 9:
            # 5. 그 줄을 통째로 출력한다 (strip() 으로 줄 끝 줄바꿈을 뗀다)
            print(line.strip())

# 도전 2-7 · WARN 인 줄만 세기
# 이 코드에서 하는 일: 등급이 WARN 인 줄이 몇 개인지 센다
# 왜 하나: 정규식 없이 in 으로도 원하는 줄을 골라낼 수 있는지 확인한다
print("---- 도전 2-7 ----")

# 1. 셀 숫자를 반복 전에 0 으로 만든다
warn_count = 0

# 2. 로그 파일을 연다
with open("raw_logs.txt", "r", encoding="utf-8") as f:
    # 3. 파일을 한 줄씩 반복한다
    for line in f:
        # 4. 줄 안에 " WARN " 이 들어 있으면 (앞뒤 빈칸까지 넣어 단어로만 찾는다)
        if " WARN " in line:
            # 5. 1 을 더한다
            warn_count += 1

# 6. 반복이 끝난 뒤 한 번만 출력한다
print("WARN", warn_count, "줄")
