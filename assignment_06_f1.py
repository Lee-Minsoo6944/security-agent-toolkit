# 1. check.txt 파일에 "점검 시작"과 "점검 끝"을 각각 다른 줄에 씁니다.
with open("check.txt", "w", encoding="utf-8") as f:
    f.write("점검 시작\n")  # 첫 번째 줄에 쓰고 줄바꿈
    f.write("점검 끝\n")   # 두 번째 줄에 쓰고 줄바꿈

print("--- check.txt 파일 작성 완료 ---")

# 2. 방금 만든 파일을 다시 읽어서 제대로 쓰였는지 확인합니다.
with open("check.txt", encoding="utf-8") as f:
    print(f.read(), end="")