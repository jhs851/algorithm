answer = 0
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def go(day, s):
    global answer

    if day > n:
        return

    if day == n:
        if answer < s:
            answer = s
        return

    go(day + a[day][0], s + a[day][1])
    go(day + 1, s)


go(0, 0)
print(answer)
