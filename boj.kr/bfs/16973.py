import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
n, m = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]
s = [[0] * (m + 1) for _ in range(n + 1)]
d = [[-1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    a[i][1:] = list(map(int, sys.stdin.readline().split()))

h, w, sr, sc, fr, fc = map(int, input().split())
queue = deque([(sr, sc)])
d[sr][sc] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + a[i][j]

while queue:
    r, c = queue.popleft()

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        # 격자판을 벗어나면 안된다
        if 1 <= nr and nr + h - 1 <= n and 1 <= nc and nc + w - 1 <= m:
            # 직사각형은 벽을 포함할 수 없다
            if s[nr + h - 1][nc + w - 1] - s[nr - 1][nc + w - 1] - s[nr + h - 1][nc - 1] + s[nr - 1][nc - 1] == 0:
                if d[nr][nc] == -1:
                    d[nr][nc] = d[r][c] + 1
                    queue.append((nr, nc))

print(d[fr][fc])