# 1. 점화식 정의 -> d[i] = i번째까지 더한 가장 큰 수
# 2. 작은 문제
# 3. 점화식 -> d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + a[i][j]
# 4. 시간복잡도 -> O(N^2)
# 5. 코드
import sys

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
d[0][0] = a[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            d[i][j] = a[i][j] + d[i - 1][j]
        elif j == i:
            d[i][j] = a[i][j] + d[i - 1][j - 1]
        else:
            d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + a[i][j]

print(max(d[n - 1]))
