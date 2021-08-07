def can_build_wall(answer):
    for x, y, a in answer:
        if a == 0:
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합
            if y != 0 and [x - 1, y, 1] not in answer and [x, y, 1] not in answer and [x, y - 1, a] not in answer:
                return False
        else:
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합
            if [x, y - 1, 0] not in answer and [x + 1, y - 1, 0] not in answer and ([x - 1, y, a] not in answer or [x + 1, y, a] not in answer):
                return False

    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b:
            answer.append([x, y, a])

            if not can_build_wall(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])

            if not can_build_wall(answer):
                answer.append([x, y, a])

    return sorted(answer, key=lambda item: (item[0], item[1], item[2]))


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]) == [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0],
                                      [5, 1, 0]])
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]) == [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]])
