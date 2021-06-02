k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    stack_map = [[[] for _ in range(n)] for _ in range(n)]
    turn = 1

    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        stack_map[r][c].append(i)

    while turn <= 1000:
        for horse_index in range(len(horse_location_and_directions)):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 이동할 칸이 파란색이거나 범위를 벗어났다면 반대로
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 이동할 말들
            move_horse_index_array = []
            for i in range(len(stack_map[r][c])):
                if stack_map[r][c][i] == horse_index:
                    move_horse_index_array = stack_map[r][c][i:]
                    stack_map[r][c] = stack_map[r][c][:i]
                    break

            # 이동할 칸이 빨간색이면 뒤집기
            if game_map[new_r][new_c] == 1:
                move_horse_index_array = reversed(move_horse_index_array)

            # 이동
            for move_horse_index in move_horse_index_array:
                stack_map[new_r][new_c].append(move_horse_index)
                horse_location_and_directions[move_horse_index][0], horse_location_and_directions[move_horse_index][1] = new_r, new_c

                if len(stack_map[new_r][new_c]) >= 4:
                    return turn

        turn += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))