import sys
from collections import deque

answer = -1
n, m = map(int, input().split())
a = [sys.stdin.readline() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
d = [[[[-1] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
x1, y1, x2, y2 = -1, -1, -1, -1
queue = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == "S":
            for k in range(4):
                queue.append((i, j, k, 0))
                d[i][j][k][0] = 0
        elif a[i][j] == "C":
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j

while queue:
    x, y, bd, c = queue.popleft()

    if c == 3:
        answer = d[x][y][bd][c]
        break

    for k in range(4):
        if bd == k:
            continue

        nx, ny, nc = x + dx[k], y + dy[k], c

        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] != "#":
                if a[nx][ny] == "C":
                    if nx == x1 and ny == y1:
                        nc |= 1
                    else:
                        nc |= 2

                if d[nx][ny][k][nc] == -1:
                    d[nx][ny][k][nc] = d[x][y][bd][c] + 1
                    queue.append((nx, ny, k, nc))

print(answer)
