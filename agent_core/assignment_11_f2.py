import json

with open("gichan_input.json", "r", encoding="utf-8") as f:
    records = json.load(f)

total = len(records)
fail = 0
for record in records:
    if record["result"] == "FAIL":
        fail += 1

message = f"전체 {total}건, 실패 {fail}건"

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(message + "\n")

print(message)