def summarize(numbers):
    total = sum(numbers)
    return f"합계 {total}"

# 결과를 report.txt에 저장
result = summarize([2, 3])

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(result)

print(result)