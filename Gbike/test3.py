def solution(day, k):
    answer = []
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = 0

    for index, month in months:
        temp = days + k

        answer.append(1 if temp % (day + 1) <= 1 else 0)

        days += month

    return answer


print(solution(6, 1))  # 100100100100
print(solution(6, 25))  # 011001000010
