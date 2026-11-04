import time

logs = [
    {"time": "09:01", "user": "kim01", "event": "LOGIN_OK", "ip": "10.0.3.21"},
    {"time": "09:05", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
    {"time": "09:12", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
    {"time": "09:18", "user": "lee02", "event": "LOGIN_FAIL", "ip": "10.0.7.5"},
    {"time": "09:21", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
]

print(logs[1]["user"])

report = {
    "admin": {"fail": 3, "ip": "10.0.9.8"},
    "lee02": {"fail": 1, "ip": "10.0.7.5"},
}

# 1. 숫자를 담을 변수를 반복 전에 만들고 0을 넣습니다.
total_fail = 0

# 2. 반복문을 돌며 실패 횟수를 누적합니다
for user, info in report.items():
    if info["fail"] > 0:
        total_fail += info["fail"]  # 조건에 맞는 값들을 더해 다시 담습니다

# 3. 반복이 끝난 뒤 결과 출력은 한 번만 합니다.
print(f"실패 {total_fail}건")

report = {
    "admin":{"fail":3, "ip":"10.0.9.8"},
    "lee02":{"fail":1, "ip":"10.0.7.5"}
}

print(report["admin"]["fail"])