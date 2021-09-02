# 나이트, 비숍, 룩 중에 선택해서 1에 놓는다
# 1초에 할 수 있는 행동은 움직이거나, 다른 말로 변경한다.
# 방문했던 곳을 다시 방문할 수 도 있고, 차례가 아닌 다른 숫자라도 방문할 수 있다.
# 0 나이트, 1 비숍, 2 룩 이라고 가정
import sys
from collections import deque

answer = -1
n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = [[[[-1] * (n * n) for _ in range(3)] for _ in range(n)] for _ in range(n)]
dx1 = [-1, -2, -2, -1, 1, 2, 2, 1]
dy1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, 1, -1]
dx3 = [1, -1, 0, 0]
dy3 = [0, 0, 1, -1]
queue = deque()

for i in range(n):
    for j in range(n):
        a[i][j] -= 1

        if a[i][j] == 0:
            for k in range(3):
                queue.append((i, j, k, 0))
                d[i][j][k][0] = 0

while queue:
    x, y, h, s = queue.popleft()

    if s == n * n - 1:
        if answer == -1 or answer > d[x][y][h][s]:
            answer = d[x][y][h][s]
        continue

    # 말 바꾸기
    for i in range(3):
        if i == h:
            continue

        if d[x][y][i][s] == -1:
            queue.append((x, y, i, s))
            d[x][y][i][s] = d[x][y][h][s] + 1

    if h == 0:  # 나이트
        for i in range(8):
            nx, ny, ns = x + dx1[i], y + dy1[i], s

            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == s + 1:
                    ns = s + 1

                if d[nx][ny][h][ns] == -1:
                    queue.append((nx, ny, h, ns))
                    d[nx][ny][h][ns] = d[x][y][h][s] + 1
    elif h == 1:  # 비숍
        for i in range(4):
            step = 1

            while True:
                nx, ny, ns = x + (dx2[i] * step), y + (dy2[i] * step), s

                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == s + 1:
                        ns = s + 1

                    if d[nx][ny][h][ns] == -1:
                        queue.append((nx, ny, h, ns))
                        d[nx][ny][h][ns] = d[x][y][h][s] + 1

                    step += 1
                else:
                    break
    else:  # 룩
        for i in range(4):
            step = 1

            while True:
                nx, ny, ns = x + (dx3[i] * step), y + (dy3[i] * step), s

                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == s + 1:
                        ns = s + 1

                    if d[nx][ny][h][ns] == -1:
                        queue.append((nx, ny, h, ns))
                        d[nx][ny][h][ns] = d[x][y][h][s] + 1

                    step += 1
                else:
                    break

print(answer)

