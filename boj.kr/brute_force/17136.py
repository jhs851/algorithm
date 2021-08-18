n = 10
colored_papers = [0, 5, 5, 5, 5, 5]
paper = [list(map(int, input().split())) for _ in range(10)]


def go(z):
    if n * n == z:
        for i in range(n):
            for j in range(n):
                if paper[i][j] == 1:
                    return -1

        return 0

    x, y = divmod(z, 10)

    if paper[x][y] == 0:
        return go(z + 1)

    answer = -1

    for k in range(5, 0, -1):
        if colored_papers[k] > 0:
            if x + k - 1 < n and y + k - 1 < n:
                ok = True

                for i in range(x, x + k):
                    for j in range(y, y + k):
                        if paper[i][j] == 0:
                            ok = False
                            break

                    if not ok:
                        break

                if ok:
                    for i in range(x, x + k):
                        for j in range(y, y + k):
                            paper[i][j] = 0

                    colored_papers[k] -= 1
                    temp = go(z + 1)
                    colored_papers[k] += 1

                    if temp != -1:
                        if answer == -1 or answer > temp + 1:
                            answer = temp + 1

                    for i in range(x, x + k):
                        for j in range(y, y + k):
                            paper[i][j] = 1

    return answer


print(go(0))
