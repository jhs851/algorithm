n, m = map(int, input().split())
c = [False] * (n + 1)
a = [0] * m


def go(index):
    if index == m:
        return print(*a)

    for i in range(1, n + 1):
        if c[i]:
            continue

        c[i] = True
        a[index] = i
        go(index + 1)
        c[i] = False


go(0)
