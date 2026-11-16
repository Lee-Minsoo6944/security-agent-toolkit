# 비정형 로그 → 쉼표 같은 정해진 칸이 없는 문장이라 split(",")처럼 위치로는 나눌 수 없다
# 정규표현식 → 몇 번째 칸인지 대신 "숫자.숫자.숫자.숫자"처럼 생긴 것을 찾아 꺼낸다

import re

csv_line = "09:05,admin,LOGIN_FAIL,10.0.9.8"
print(csv_line.split(","))

raw_line = "Nov 16 09:05:12 sshd: Failed password for admin from 10.0.9.8 port 22"
print(raw_line.split(","))

ip = re.search(r"\d+\.\d+\.\d+\.\d+", raw_line)
print("IP:", ip.group())

user = re.search(r"for (\w+) from", raw_line)
print("계정:", user.group(1))
