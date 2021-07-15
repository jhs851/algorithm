import sys


# DFS 문제라고 생각
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # 북 서 남 동
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
    # r, c, turn
    stack = [(0, 0, 0)]
    min_turn = sys.maxsize

    while stack:
        r, c, turn = stack.pop()
        new_turn = turn + 1

        for i in range(4):
            new_r, new_c = r + dr[i], c + dc[i]

            if new_r == n - 1 and new_c == m - 1 and new_turn < min_turn:
                min_turn = new_turn
            elif new_r < n and new_c < m and maps[new_r][new_c] == 1:
                stack.append((new_r, new_c, new_turn))
                maps[new_r][new_c] = 2

    return min_turn


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
