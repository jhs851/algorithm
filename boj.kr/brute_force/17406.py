import sys
from itertools import permutations

answer = sys.maxsize
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(k)]

for case in permutations(b, k):
    _a = [row[:] for row in a]

    for r, c, s in case:
        __a = [row[:] for row in _a]
        r, c = r - 1, c - 1

        for i in range(1, s + 1):
            # 위
            for j in range(c - i, c + i):
                new_r = r - i

                if j == c - i:
                    _a[new_r][j] = __a[new_r + 1][j]
                else:
                    _a[new_r][j] = __a[new_r][j - 1]

            # 오른쪽
            for j in range(r - i, r + i):
                new_c = c + i

                if j == r - i:
                    _a[j][new_c] = __a[j][new_c - 1]
                else:
                    _a[j][new_c] = __a[j - 1][new_c]

            # 아래
            for j in range(c + i, c - i, -1):
                new_r = r + i

                if j == c + i:
                    _a[new_r][j] = __a[new_r - 1][j]
                else:
                    _a[new_r][j] = __a[new_r][j + 1]

            # 왼쪽
            for j in range(r + i, r - i, -1):
                new_c = c - i

                if j == r + i:
                    _a[j][new_c] = __a[j][new_c + 1]
                else:
                    _a[j][new_c] = __a[j + 1][new_c]

    sum_a = min([sum(row) for row in _a])

    if answer > sum_a:
        answer = sum_a

print(answer)

# 5 6 2
# 1 2 3 2 5 6
# 3 8 7 2 1 3
# 8 2 3 1 4 5
# 3 4 5 1 1 1
# 9 3 2 1 4 3
# 3 4 2
# 4 2 1
# 12
