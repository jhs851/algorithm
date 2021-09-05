import sys

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = sys.maxsize

        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + a[j][0] * a[k][1] * a[x][1])

print(dp[0][n - 1])
