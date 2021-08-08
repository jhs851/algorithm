n, m = map(int, input().split())
exclude = [[False] * n for _ in range(n)]
answer = 0

for _ in range(m):
    i, j = map(int, input().split())
    exclude[i - 1][j - 1] = exclude[j - 1][i - 1] = True

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if exclude[i][j] or exclude[j][k] or exclude[k][i]:
                continue
            answer += 1

print(answer)
