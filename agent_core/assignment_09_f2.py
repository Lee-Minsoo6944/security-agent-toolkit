def check(fail_count):
  if fail_count >= 3:
    return "추가 확인"
  else:
    return "기록 유지"
# 경계 확인을 위해 2와 3을 각각 인자로 넣어 호출
print(check(2))
print(check(3))