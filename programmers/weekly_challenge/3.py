def rotate(piece):
    n, m = len(piece), len(piece[0])
    rotated = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotated[j][n - i - 1] = piece[i][j]

    return rotated


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                game_board[i][j] = 2
            if table[i][j] == 1:
                table[i][j] = 2
            elif table[i][j] == 0:
                table[i][j] = 1

    blanks = []
    visited1 = [[False] * n for _ in range(n)]
    pieces = []
    visited2 = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 2 and not visited1[i][j]:
                s = [(i, j)]
                visited1[i][j] = True
                blank = [i, j, i, j]

                while s:
                    x, y = s.pop()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and game_board[nx][ny] == 2 and not visited1[nx][ny]:
                            s.append((nx, ny))
                            visited1[nx][ny] = True
                            minx, miny, maxx, maxy = blank
                            blank = [min(minx, nx), min(miny, ny), max(maxx, nx), max(maxy, ny)]

                minx, miny, maxx, maxy = blank
                blanks.append([row[miny:maxy + 1] for row in game_board[minx:maxx + 1]])

            if table[i][j] == 2 and not visited2[i][j]:
                s = [(i, j)]
                visited2[i][j] = True
                piece = [i, j, i, j]

                while s:
                    x, y = s.pop()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and table[nx][ny] == 2 and not visited2[nx][ny]:
                            s.append((nx, ny))
                            visited2[nx][ny] = True
                            minx, miny, maxx, maxy = piece
                            piece = [min(minx, nx), min(miny, ny), max(maxx, nx), max(maxy, ny)]

                minx, miny, maxx, maxy = piece
                pieces.append([row[miny:maxy + 1] for row in table[minx:maxx + 1]])

    for blank in blanks:
        ok = False

        for i in range(len(pieces)):
            piece = pieces[i]

            for _ in range(4):
                if blank == piece:
                    answer += sum([len([True for num in p if num == 2]) for p in piece])
                    pieces.pop(i)
                    ok = True

                if ok:
                    break

                piece = rotate(piece)

            if ok:
                break

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))  # 14
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))  # 0

