from collections import deque

# 오른쪽위, 오른쪽, 아래, 왼쪽아래, 왼쪽, 위
dx = [-1, 0, 1, 1, 0, -1]
dy = [1, 1, 0, -1, -1, 0]
n = 1156
a = [[0] * n for _ in range(n)]
x, y = n // 2, n // 2
a[x][y] = 1
num = 2
MAX = 1000519
coords = [None] * (MAX + 1)

for i in range(1, 578):
    x += dx[5]
    y += dy[5]
    a[x][y] = num
    num += 1

    for j in range(6):
        k = i

        if j == 0:
            k -= 1

        for _ in range(k):
            x += dx[j]
            y += dy[j]
            a[x][y] = num
            num += 1

for i in range(n):
    for j in range(n):
        if a[i][j] != 0 and a[i][j] <= MAX:
            coords[a[i][j]] = (i, j)

en, st = map(int, input().split())
q = deque([st])
d = [-1] * (MAX + 1)
b = [-1] * (MAX + 1)
d[st] = 0

while q:
    now = q.popleft()
    x, y = coords[now]

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] != 0:
                nxt = a[nx][ny]

                if d[nxt] == -1:
                    q.append(nxt)
                    d[nxt] = d[now] + 1
                    b[nxt] = now

print(en, end=" ")
while en != st:
    en = b[en]
    print(en, end=" ")