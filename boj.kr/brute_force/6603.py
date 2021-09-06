while True:
    n = list(map(int, input().split()))

    if n[0] == 0:
        break

    a = n[1:]
    n = n[0]
    v = [False] * n
    answer = [0] * 6

    def go(start, index):
        if index == 6:
            return print(*answer)

        for i in range(start, n):
            if v[i]:
                continue

            v[i] = True
            answer[index] = a[i]
            go(i, index + 1)
            v[i] = False

    go(0, 0)
    print()
