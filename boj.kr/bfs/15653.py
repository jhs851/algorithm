from collections import deque

answer = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
d = [[[[-1] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
a = [list(input()) for _ in range(n)]
queue = deque()
r, b, h = None, None, None

for i in range(n):
    for j in range(m):
        if a[i][j] == "R":
            r = (i, j)
            a[i][j] = "."
        elif a[i][j] == "B":
            b = (i, j)
            a[i][j] = "."
        elif a[i][j] == "O":
            h = (i, j)

queue.append((r[0], r[1], b[0], b[1]))
d[r[0]][r[1]][b[0]][b[1]] = 0

while queue:
    rx, ry, bx, by = queue.popleft()

    for i in range(4):
        nrx, nry = rx, ry
        nbx, nby = bx, by
        rmc, bmc = 0, 0

        while a[nrx + dx[i]][nry + dy[i]] != "#":
            nrx, nry = nrx + dx[i], nry + dy[i]
            rmc += 1

            if a[nrx][nry] == "O":
                break

        while a[nbx + dx[i]][nby + dy[i]] != "#":
            nbx, nby = nbx + dx[i], nby + dy[i]
            bmc += 1

            if a[nbx][nby] == "O":
                break

        # 파란 공이 구멍에 있을 때
        if a[nbx][nby] == "O":
            continue

        # 공이 겹쳤을 때
        if nrx == nbx and nry == nby:
            # 더 많이 움직인 공을 지금 방향 반대로 한칸
            # 빨간 공이 더 많이 움직였을 때
            if rmc > bmc:
                nrx, nry = nrx - dx[i], nry - dy[i]
            # 파란 공이 현재 방향에서 더 멀 때
            else:
                nbx, nby = nbx - dx[i], nby - dy[i]

        # 빨간 공만 구멍에 있을 때
        if a[nrx][nry] == "O":
            if answer == -1 or answer > d[rx][ry][bx][by] + 1:
                answer = d[rx][ry][bx][by] + 1
        # 현재 위치가 처음일 때
        elif d[nrx][nry][nbx][nby] == -1:
            queue.append((nrx, nry, nbx, nby))
            d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1

print(answer)

