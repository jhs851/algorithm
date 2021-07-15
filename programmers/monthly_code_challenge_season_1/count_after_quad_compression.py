def solution(arr):
    def check(r, c, n):
        if n == 1:
            return [0, 1] if arr[r][c] == 1 else [1, 0]

        left_up = check(r, c, n // 2)
        right_up = check(r, c + n // 2, n // 2)
        left_down = check(r + n // 2, c, n // 2)
        right_down = check(r + n // 2, c + n // 2, n // 2)

        if left_up == right_up == left_down == right_down == [0, 1] or left_up == right_up == left_down == right_down == [1, 0]:
            return left_up
        else:
            return list(map(sum, zip(left_up, right_up, left_down, right_down)))

    return check(0, 0, len(arr))


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))  # [4,9]
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))  # [10,15]
