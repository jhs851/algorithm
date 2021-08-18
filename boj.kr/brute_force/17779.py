import sys


def fill_district(r, c, fill, city):
    n = len(city)
    city[r][c] = fill
    stack = [(r, c)]
    d_r = [-1, 0, 1, 0]
    d_c = [0, -1, 0, 1]

    while stack:
        _r, _c = stack.pop()

        for i in range(4):
            new_r, new_c = _r + d_r[i], _c + d_c[i]

            if 0 <= new_r < n and 0 <= new_c < n and city[new_r][new_c] == 0:
                stack.append((new_r, new_c))
                city[new_r][new_c] = fill


def get_difference(x, y, d1, d2, peoples):
    n = len(peoples)
    city = [[0] * n for _ in range(n)]

    # 마름모 그리기
    for i in range(d1 + 1):
        city[x + i][y - i] = 5
        city[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1):
        city[x + i][y + i] = 5
        city[x + d1 + i][y - d1 + i] = 5

    # 다른 선거구 경계선
    for i in range(x):
        city[i][y] = 1

    for i in range(y + d2 + 1, n):
        city[x + d2][i] = 2

    for i in range(y - d1):
        city[x + d1][i] = 3

    for i in range(x + d1 + d2 + 1, n):
        city[i][y - d1 + d2] = 4

    # 선거구 채우기
    fill_district(0, 0, 1, city)
    fill_district(0, n - 1, 2, city)
    fill_district(n - 1, 0, 3, city)
    fill_district(n - 1, n - 1, 4, city)

    peoples_count = [0] * 5
    for i in range(n):
        for j in range(n):
            if city[i][j] == 0:
                city[i][j] = 5

            peoples_count[city[i][j] - 1] += peoples[i][j]

    peoples_count.sort()
    return peoples_count[-1] - peoples_count[0]


answer = sys.maxsize
n = int(input())
peoples = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if y - d1 >= 0 and y + d2 < n and x + d1 + d2 < n:
                    difference = get_difference(x, y, d1, d2, peoples)

                    if answer > difference:
                        answer = difference

print(answer)


