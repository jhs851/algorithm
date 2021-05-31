from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    seconds = 0
    queue = deque()
    queue.append((brown_loc, seconds))
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += seconds

        if cony_loc in visited[seconds]:
            return seconds

        for i in range(len(queue)):
            current_position, current_seconds = queue.popleft()

            new_seconds = current_seconds + 1
            new_position = current_position - 1
            if new_position >= 0 and new_position not in visited[new_seconds]:
                visited[new_seconds][new_position] = True
                queue.append((new_position, new_seconds))

            new_position = current_position + 1
            if new_position <= 200000 and new_position not in visited[new_seconds]:
                visited[new_seconds][new_position] = True
                queue.append((new_position, new_seconds))

            new_position = current_position * 2
            if new_position <= 200000 and new_position not in visited[new_seconds]:
                visited[new_seconds][new_position] = True
                queue.append((new_position, new_seconds))

        seconds += 1

    return seconds


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
