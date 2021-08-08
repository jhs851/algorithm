d_r = [-1, 0, 1, 0]
d_c = [0, -1, 0, 1]
board = [list(map(int, input().split())) for _ in range(5)]
answer = set()

for i in range(5):
    for j in range(5):
        stack = [(i, j, str(board[i][j]))]

        while stack:
            r, c, attached = stack.pop()

            for k in range(4):
                new_r, new_c = r + d_r[k], c + d_c[k]

                if not 0 <= new_r < 5 or not 0 <= new_c < 5:
                    continue

                new_attached = attached + str(board[new_r][new_c])

                if len(new_attached) == 6:
                    answer.add(new_attached)
                    continue

                stack.append((new_r, new_c, new_attached))

print(len(answer))

# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 2 1
# 1 1 1 1 1
# 15
