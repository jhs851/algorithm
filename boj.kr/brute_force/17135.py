from itertools import combinations

answer = 0
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for archers in combinations([(n, i) for i in range(m)], 3):
    kills = 0
    _board = [row[:] for row in board]

    while True:
        has_enemy = False

        for i in range(n):
            for j in range(m):
                if _board[i][j] == 1:
                    has_enemy = True

        if not has_enemy:
            break

        deleted = [(-1, -1)] * 3
        for i in range(3):
            r1, c1 = archers[i]
            d1 = -1

            for c2 in range(m):
                for r2 in range(n):
                    if _board[r2][c2] == 1:
                        distance = abs(r1 - r2) + abs(c1 - c2)

                        if distance <= d and (d1 == -1 or d1 > distance):
                            deleted[i] = (r2, c2)
                            d1 = distance

        for r, c in deleted:
            if r == -1:
                continue

            if _board[r][c] == 1:
                kills += 1
                _board[r][c] = 0

        # 적들 내리기
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == 0:
                    _board[i][j] = 0
                else:
                    _board[i][j] = _board[i - 1][j]

    if kills > answer:
        answer = kills

print(answer)

# 5 5 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 1 1 1 1
# 3
