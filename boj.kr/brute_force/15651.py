n, m = map(int, input().split())
a = [0] * m


def go(index):
    if index == m:
        return print(*a)

    for i in range(1, n + 1):
        a[index] = i
        go(index + 1)


go(0)
