from collections import deque


def check(row, col, place):
    direct_row = [-1, 0, 1, 0]
    direct_col = [0, -1, 0, 1]
    visited = {(row, col)}
    queue = deque()
    queue.append((row, col, 0))

    while queue:
        r, c, count = queue.popleft()

        if count == 2:
            continue

        for i in range(4):
            new_row, new_col = r + direct_row[i], c + direct_col[i]

            if 0 <= new_row < 5 and 0 <= new_col < 5 and (new_row, new_col) not in visited:
                if place[new_row][new_col] == "P":
                    return False
                elif place[new_row][new_col] == "X":
                    continue

                queue.append((new_row, new_col, count + 1))
                visited.add((new_row, new_col))

    return True


def solution(places):
    answer = []

    for place in places:
        candidates = []

        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == "P":
                    candidates.append((i, j))

        for row, col in candidates:
            if not check(row, col, place):
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))  # [1, 0, 1, 1, 1]
