def show_alert(user):
    print(f"{user} 계정을 확인하세요")

show_alert("kim01")
show_alert("park03")

def show_count(user, count):
    print(f"{user}: {count}회")

show_count("kim01", 3)

def add(a, b):
    return a + b

result = add(3, 5)
print(result)


logs = [
    {"result": "FAIL"}, {"result": "OK"},
    {"result": "FAIL"}, {"result": "FAIL"},
]

def count_failed(logs):
    fail_count = 0
    for log in logs:
        if log["result"] == "FAIL":
            fail_count = fail_count + 1
    return fail_count

total = count_failed(logs)
print(f"실패 {total}건")


def greet(name):
  return f"안녕하세요 {name}"


# 함수를 두 번 호출하여 결과를 각각 출력
print(greet("기찬"))
print(greet("정민"))