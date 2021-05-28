from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 북 = 0 / 동 = 1 / 남 = 2 / 서 = 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 북 -> 서 = 0 -> 3
# 서 -> 남 = 3 -> 2
# 남 -> 동 = 2 -> 1
# 동 -> 북 = 1 -> 0
def get_direction_index_when_rotate_left(direction):
    return (direction + 3) % 4


# 북 -> 남 = 0 -> 2
# 서 -> 동 = 3 -> 1
# 남 -> 북 = 2 -> 0
# 동 -> 서 = 1 -> 3
def get_direction_index_when_go_back(direction):
    return (direction + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cleaned_count = 1
    room_map[r][c] = 2
    queue = deque()
    queue.append([r, c, d])

    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        for i in range(4):
            temp_d = get_direction_index_when_rotate_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if room_map[new_r][new_c] == 0:
                room_map[new_r][new_c] = 2
                cleaned_count += 1
                queue.append([new_r, new_c, temp_d])
                break
            elif i == 3:
                new_r, new_c = r + dr[get_direction_index_when_go_back(temp_d)], c + dc[get_direction_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])

                if room_map[new_r][new_c] == 1:
                    return cleaned_count

    return cleaned_count


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
