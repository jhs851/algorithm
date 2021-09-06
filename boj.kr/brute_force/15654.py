n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
c = [False] * n
answer = [0] * m


def go(index):
    if index == m:
        return print(*answer)

    for i in range(n):
        if c[i]:
            continue

        c[i] = True
        answer[index] = a[i]
        go(index + 1)
        c[i] = False


go(0)
