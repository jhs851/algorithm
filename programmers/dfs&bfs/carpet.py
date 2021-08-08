def solution(brown, yellow):
    s = brown + yellow

    for i in range(s, 2, -1):
        if s % i == 0:
            c = s // i

            if yellow == (i - 2) * (c - 2):
                return [i, c]


print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]
print(solution(12, 3))  # [5, 3]
