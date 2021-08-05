import sys


def check(office, r, c, d):
    n, m = len(office), len(office[0])
    d_r = [-1, 0, 1, 0]
    d_c = [0, -1, 0, 1]

    while 0 <= r < n and 0 <= c < m:
        if office[r][c] == 6:
            break

        office[r][c] = "#"
        r += d_r[d]
        c += d_c[d]


def go(office, cameras, index, dirs):
    if len(cameras) == index:
        n, m = len(office), len(office[0])
        _office = [row[:] for row in office]

        for i, (kind, r, c) in enumerate(cameras):
            if kind == 1:
                check(_office, r, c, dirs[i])
            elif kind == 2:
                check(_office, r, c, dirs[i])
                check(_office, r, c, (dirs[i] + 2) % 4)
            elif kind == 3:
                check(_office, r, c, dirs[i])
                check(_office, r, c, (dirs[i] + 1) % 4)
            elif kind == 4:
                check(_office, r, c, dirs[i])
                check(_office, r, c, (dirs[i] + 1) % 4)
                check(_office, r, c, (dirs[i] + 2) % 4)
            elif kind == 5:
                check(_office, r, c, dirs[i])
                check(_office, r, c, (dirs[i] + 1) % 4)
                check(_office, r, c, (dirs[i] + 2) % 4)
                check(_office, r, c, (dirs[i] + 3) % 4)

        count = 0

        for i in range(n):
            for j in range(m):
                if _office[i][j] == 0:
                    count += 1

        return count

    answer = sys.maxsize

    for i in range(4):
        temp = go(office, cameras, index + 1, dirs + [i])

        if answer > temp:
            answer = temp

    return answer


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cameras = []

for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cameras.append((office[i][j], i, j))

print(go(office, cameras, 0, []))

# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0
# 20

# 6 6
# 0 0 0 0 0 0
# 0 2 0 0 0 0
# 0 0 0 0 6 0
# 0 6 0 0 2 0
# 0 0 0 0 0 0
# 0 0 0 0 0 5
# 15

# 6 6
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1
# 6

# 6 6
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 5 0 0
# 0 0 5 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1
# 2

# 1 7
# 0 1 2 3 4 5 6
# 0

# 3 7
# 4 0 0 0 0 0 0
# 0 0 0 2 0 0 0
# 0 0 0 0 0 0 4
# 0
