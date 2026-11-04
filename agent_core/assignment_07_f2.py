groups = [[2, 1], [3, 0]]

# 바깥쪽 반복문: 각 묶음(group)을 하나씩 가져옴
for group in groups:
    total = 0  # 💡 각 묶음의 합을 계산하기 전에 0으로 초기화
    
    # 안쪽 반복문: 묶음 안의 숫자(num)를 하나씩 더함
    for num in group:
        total += num
        
    # 묶음 하나의 합계 출력
    print(total)