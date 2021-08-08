import copy


def solution(key, lock):
    n, m = len(lock), len(key)
    matrix = [[0] * (n + (m - 1) * 2) for _ in range(n + (m - 1) * 2)]

    for i in range(n):
        for j in range(n):
            matrix[i + m - 1][j + m - 1] = lock[i][j]

    # 돌리기
    for _ in range(3):
        # 움직이기
        for row in range(n + m - 1):
            for col in range(n + m - 1):
                # 확인하기
                check = copy.deepcopy(matrix)

                for i in range(m):
                    for j in range(m):
                        if check[row + i][col + j] == 1:
                            continue
                        elif key[i][j] == 1:
                            check[row + i][col + j] = 1

                for i in range(n):
                    if 0 in check[i + m - 1][m - 1:m + n - 1]:
                        break
                else:
                    return True

        rotate = copy.deepcopy(key)
        for i in range(m):
            for j in range(m):
                rotate[j][m - i - 1] = key[i][j]
        key = rotate

    return False


# [
#     [1, 1, 1],
#     [1, 1, 0],
#     [1, 0, 1]
# ]

# [
#     [0, 0, 0],
#     [1, 0, 0],
#     [0, 1, 1]
# ]

# [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ]

# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 1, 1, 1, 0, 0],
# [0, 0, 1, 1, 1, 0, 0],
# [0, 0, 1, 1, 1, 0, 0],
# [0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0]


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))  # True
print(solution([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))  # True
