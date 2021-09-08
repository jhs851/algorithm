# 1. 점화식 정의 -> N번째 집까지 색을 칠하는 최소 비용
# 2. 작은 문제
#   -> d[i][j] = i번째 집까지 j색을 칠하는 최소 비용
# 3. 점화식 -> d[i][j] = min(d[i-1][!j] + a[i][j])
# 4. 시간복잡도 -> O(N)
# 5. 코드
import sys

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[0] * 3 for _ in range(n)]
d[0][0] = a[0][0]
d[0][1] = a[0][1]
d[0][2] = a[0][2]

for i in range(1, n):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + a[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + a[i][2]

print(min(d[n - 1]))
