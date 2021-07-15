def should_explod(m, n, board):
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] is not None and board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1]:
                return True

    return False


def solution(m, n, board):
    answer = 0

    # board를 2차원 배열로
    for i in range(m):
        board[i] = list(board[i])

    while should_explod(m, n, board):
        exploded_index_array = set()

        # 터트려야할 인덱스들 저장
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] is not None and board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1]:
                    exploded_index_array.add((i, j))
                    exploded_index_array.add((i - 1, j))
                    exploded_index_array.add((i, j - 1))
                    exploded_index_array.add((i - 1, j - 1))

        answer += len(exploded_index_array)

        # 터트리기
        for exploded_index in exploded_index_array:
            r, c = exploded_index
            board[r][c] = None

        # 남은 것들 내려보내기
        for i in range(1, m):
            for j in range(n):
                if board[i][j] is None and board[i - 1][j] is not None:
                    board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
