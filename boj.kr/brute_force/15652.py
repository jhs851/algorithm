n, m = map(int, input().split())
a = [0] * m


def go(index, before):
    if index == m:
        return print(*a)

    for i in range(1, n + 1):
        if i >= before:
            a[index] = i
            go(index + 1, i)


go(0, 0)
