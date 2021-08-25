# (N^2 * NM) + (M^2 * NM)
# -> 이건 너무 큼...

# 5x4 배열이 있다고 할 때 B를 만들기 위해 더한 횟수는 다음과 같음
# 1 2 2 2 1
# 2 4 4 4 2
# 2 4 4 4 2
# 1 2 2 2 1
# 열에서 0과 n-1열 둘 중 합이 가장 큰 열과
# 1 ~ n-2 에서 합이 가장 작은 열과 교체.
# 그 후에 B 배열의 합을 구한다.
# 행도 같음
import sys

n, m = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def get_sum_b():
    return sum(sum(a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i][j + 1] for j in range(m - 1)) for i in range(n - 1))


def swap_row(r1, r2):
    for j in range(m):
        a[r1][j], a[r2][j] = a[r2][j], a[r1][j]


def swap_col(c1, c2):
    for i in range(n):
        a[i][c1], a[i][c2] = a[i][c2], a[i][c1]


sum_row = [0] * n
sum_col = [0] * m

for i in range(n):
    for j in range(m):
        sum_row[i] += a[i][j]
        sum_col[j] += a[i][j]

min_row = -1
for i in range(1, n - 1):
    sum_row[i] *= 4
    sum_row[i] -= 2 * (a[i][0] + a[i][m - 1])

    if min_row == -1 or sum_row[min_row] > sum_row[i]:
        min_row = i

min_col = - 1
for j in range(1, m - 1):
    sum_col[j] *= 4
    sum_col[j] -= 2 * (a[0][j] + a[n - 1][j])

    if min_col == -1 or sum_col[min_col] > sum_col[j]:
        min_col = j

answer = get_sum_b()

if min_row != -1:
    swap_row(0, min_row)
    temp = get_sum_b()
    if answer < temp:
        answer = temp
    swap_row(0, min_row)
    swap_row(n - 1, min_row)
    temp = get_sum_b()
    if answer < temp:
        answer = temp
    swap_row(n - 1, min_row)

if min_col != -1:
    swap_col(0, min_col)
    temp = get_sum_b()
    if answer < temp:
        answer = temp
    swap_col(0, min_col)
    swap_col(m - 1, min_col)
    temp = get_sum_b()
    if answer < temp:
        answer = temp

print(answer)
