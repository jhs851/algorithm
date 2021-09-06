import sys

answer = -sys.maxsize
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
v = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def go(p, c, s):
    if c == k:
        global answer
        if s > answer:
            answer = s

    for i in range(p + 1, n * m):
        x = i // m
        y = i % m

        if v[x][y]:
            continue

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]

            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny]:
                    break
        else:
            v[x][y] = True
            go(i, c + 1, s + a[x][y])
            v[x][y] = False


go(-1, 0, 0)
print(answer)
