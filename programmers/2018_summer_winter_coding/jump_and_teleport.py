# 현재 위치부터 0까지 도달하는 방법을 역산하면 간단히 식을 도출할 수 있음
def solution(n):
    ans = 0

    while n:
        quotient, remainder = divmod(n, 2)
        n = quotient

        if remainder != 0:
            ans += 1

    return ans


print(solution(5))  # 2
print(solution(6))  # 2
print(solution(5000))  # 5
