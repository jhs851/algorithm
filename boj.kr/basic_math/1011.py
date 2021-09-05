# t = int(input())

def solution(x, y):
# for _ in range(t):
    # x, y = map(int, input().split())
    count = 0
    m = 0

    while x < y:
        m += m + 1
        x += m
        count += 1

    # print(count)
    return count + 1


print(solution(0, 3))  # 3
print(solution(1, 5))  # 3
print(solution(45, 50))  # 4


# 3
# 0 3
# 1 5
# 45 50