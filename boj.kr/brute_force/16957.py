import sys
sys.setrecursionlimit(10 ** 6)

r, c = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
check = [[None] * c for _ in range(r)]
answer = [[0] * c for _ in range(r)]


def go(x, y):
    if check[x][y] is not None:
        return check[x][y]

    # 8방향중 가장 작은 곳으로
    min_v = (x, y, a[x][y])
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < r and 0 <= ny < c:
            if min_v[2] > a[nx][ny]:
                min_v = (nx, ny, a[nx][ny])

    if min_v[2] == a[x][y]:
        check[x][y] = (x, y)
    else:
        check[x][y] = go(min_v[0], min_v[1])

    return check[x][y]


for i in range(r):
    for j in range(c):
        if check[i][j] is None:
            go(i, j)

for i in range(r):
    for j in range(c):
        _r, _c = check[i][j]
        answer[_r][_c] += 1

for i in range(r):
    print(*answer[i])

