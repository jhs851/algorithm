from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, p = map(int, input().split())
answer = [0] * p
s = list(map(int, input().split()))
a = [list(input()) for _ in range(n)]
queue = [deque() for _ in range(p)]
next_queue = [deque() for _ in range(p)]

for i in range(n):
    for j in range(m):
        if a[i][j] != "." and a[i][j] != "#":
            a[i][j] = int(a[i][j]) - 1
            queue[a[i][j]].append((i, j))

while True:
    ok = False

    for i in range(p):
        d = [[0] * m for _ in range(n)]

        while queue[i]:
            ok = True
            x, y = queue[i].popleft()

            if d[x][y] == s[i]:
                next_queue[i].append((x, y))

            if a[x][y] != "." and a[x][y] != "#" and a[x][y] != i:
                continue

            a[x][y] = i

            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]

                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == ".":
                        d[nx][ny] = d[x][y] + 1

                        if d[nx][ny] <= s[i]:
                            queue[i].append((nx, ny))
                            a[nx][ny] = i

        queue[i] = next_queue[i]
        next_queue[i] = deque()

    if not ok:
        break

for i in range(n):
    for j in range(m):
        if a[i][j] != "." and a[i][j] != "#":
            answer[a[i][j]] += 1

print(*answer)
