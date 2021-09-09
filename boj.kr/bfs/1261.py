from collections import deque

m, n = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
d[0][0] = 0
q = deque([(0, 0)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny] == -1 or d[nx][ny] > d[x][y] + a[nx][ny]:
                d[nx][ny] = d[x][y] + a[nx][ny]
                q.append((nx, ny))

print(d[n - 1][m - 1])
