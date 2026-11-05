def needs_review(count, threshold=2):
    return count >= threshold
print(needs_review(3))
print(needs_review(3, 5))


def filter_values(data):
    return [x for x in data if x >= 3]

# 테스트 실행
print(filter_values([1, 2, 4, 5]))  # [4, 5]
print(filter_values([]))            # []