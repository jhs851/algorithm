def solution(n, build_frame):
    answer = []
    n += 1
    wall = [[None] * n for _ in range(n)]

    for x, y, a, b in build_frame:
        # 기둥일 때
        if a == 0:
            if b == 1:
                if y == 0 or (x > 0 and wall[y][x - 1] == 1) or (x < n - 1 and wall[y][x + 1] == 1) or (
                        y > 0 and wall[y - 1][x] == 0):
                    wall[y][x] = 0

        # 보일 때
        else:
            if b == 1:
                if (y > 0 and wall[y - 1][x] == 0) or (y > 0 and x < n - 1 and wall[y - 1][x + 1] == 0) or (0 < x < n - 1 and wall[y][x - 1] == 1 and wall[y][x + 1] == 1):
                    wall[y][x] = 1

    for y in range(n):
        for x in range(n):
            if wall[y][x] is not None:
                answer.append([x, y, wall[y][x]])

    return sorted(answer, key=lambda item: (item[0], item[1], item[2]))


# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합
# y == 0 or [y][x - 1] == 1 or [y][x + 1] == 1 or [y - 1][x] == 0

# 기둥을 삭제할 때
# 바닥이 아니고, 기둥에 걸쳐있는 보가 없고(해당 보가 다른 기둥에 걸쳐있지 않고), 다른 기둥을 받치고 있지 않아야함(해당 기둥을 받치는 보가 없어야함)
# y != 0 and

[
    [None,    0, None, None, None,    0],
    [None,    1,    0, None, None,    0],
    [None, None,    1,    1,    1, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None]
]

# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합
# [y - 1][x] == 0 or [y - 1][x + 1] == 0 or [y][x - 1] == 1 and [y][x + 1] == 1

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]) == [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0],
                                      [5, 1, 0]])
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]) == [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1],
                                                                  [4, 0, 0]])
