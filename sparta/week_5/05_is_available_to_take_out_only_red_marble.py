from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move_until_to_wall_or_hole(r, c, d, game_map):
    move_count = 0

    while game_map[r + dr[d]][c + dc[d]] != '#' and game_map[r][c] != 'O':
        r += dr[d]
        c += dc[d]
        move_count += 1

    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n = len(game_map)
    m = len(game_map[0])
    queue = deque()
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if game_map[i][j] == 'R':
                red_row, red_col = i, j
            elif game_map[i][j] == 'B':
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()

        if try_count > 10:
            break

        for i in range(4):
            new_red_row, new_red_col, red_move_count = move_until_to_wall_or_hole(red_row, red_col, i, game_map)
            new_blue_row, new_blue_col, blue_move_count = move_until_to_wall_or_hole(blue_row, blue_col, i, game_map)

            if game_map[new_blue_row][new_blue_col] == 'O':
                continue
            elif game_map[new_red_row][new_red_col] == 'O':
                return True
            else:
                if new_red_row == new_blue_row and new_red_col == new_blue_col:
                    if red_move_count > blue_move_count:
                        new_red_row -= dr[i]
                        new_red_col -= dc[i]
                    else:
                        new_blue_row -= dr[i]
                        new_blue_col -= dc[i]

                if not visited[new_red_row][new_red_col][new_blue_row][new_blue_col]:
                    visited[new_red_row][new_red_col][new_blue_row][new_blue_col] = True
                    queue.append((new_red_row, new_red_col, new_blue_row, new_blue_col, try_count + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))
