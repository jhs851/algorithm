# 판은 시계 방향, 혹은 반시계 방향으로 자유롭게 회전할 수 있다.
# 판을 쌓는 순서는 자유롭다
# 4^5 * 5! * 5^3 = 15,360,000
from copy import deepcopy
from collections import deque
from itertools import permutations

n = 5
b = [[list(map(int, input().split())) for _ in range(n)] for _ in range(n)]
answer = -1


def get_passed_count(cube):
    if cube[0][0][0] == 0:
        return -1

    d_r = [0, 0, 0, 0, 1, -1]
    d_c = [0, 0, 1, -1, 0, 0]
    d_z = [1, -1, 0, 0, 0, 0]
    queue = deque([(0, 0, 0)])
    visited = [[[-1] * n for _ in range(n)] for _ in range(n)]
    visited[0][0][0] = 0

    while queue:
        z, r, c = queue.popleft()

        for i in range(6):
            new_z, new_r, new_c = z + d_z[i], r + d_r[i], c + d_c[i]

            if not 0 <= new_z < n or not 0 <= new_r < n or not 0 <= new_c < n:
                continue

            if cube[new_z][new_r][new_c] == 1 and visited[new_z][new_r][new_c] == -1:
                queue.append((new_z, new_r, new_c))
                visited[new_z][new_r][new_c] = visited[z][r][c] + 1

    return visited[-1][-1][-1]


def rotate(board):
    rotated = [row[:] for row in board]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = board[i][j]

    return rotated


# 자유롭게 쌓기
for orders in permutations([i for i in range(n)], n):
    a = deepcopy(b)

    for i in range(len(orders)):
        a[orders[i]] = b[i]

    # 각 판별로 회전
    for _ in range(4):
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        temp = get_passed_count(a)

                        if (temp != -1) and (answer == -1 or answer > temp):
                            answer = temp

                        a[4] = rotate(a[4])
                    a[3] = rotate(a[3])
                a[2] = rotate(a[2])
            a[1] = rotate(a[1])
        a[0] = rotate(a[0])

print(answer)
