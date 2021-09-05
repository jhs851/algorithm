n, k = map(int, input().split())
d = [[[[False] * 436 for _ in range(31)] for _ in range(31)] for _ in range(31)]
answer = ""


def go(i, a, b, p):
    if i == n:
        return p == k

    if d[i][a][b][p]:
        return False

    d[i][a][b][p] = True
    global answer
    temp = answer

    answer = temp + "A"
    if go(i + 1, a + 1, b, p):
        return True

    answer = temp + "B"
    if go(i + 1, a, b + 1, p + a):
        return True

    answer = temp + "C"
    if go(i + 1, a, b, p + a + b):
        return True

    return False


if go(0, 0, 0, 0):
    print(answer)
else:
    print(-1)
