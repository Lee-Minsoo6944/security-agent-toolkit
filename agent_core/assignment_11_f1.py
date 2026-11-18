import csv

count = 0

with open("gichan_input.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["result"] == "FAIL":
            count += 1

print(count)