n, m = map(int, input().split())
c = [False] * (n + 1)
a = [0] * m


def go(num, selected):
    if selected == m:
        return print(*a)

    if num > n:
        return

    a[selected] = num
    go(num + 1, selected + 1)
    a[selected] = 0
    go(num + 1, selected)


go(1, 0)
