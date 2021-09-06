# - -2 -2 = -4
# + -2 5 = 3
# 0 -2 5 -3 = 0
# + -2 5 -3 1 = 1
# + 5 5 = 10
# + 5 -3 = 2
# + 5 -3 1 = 3
# - -3 -3 = -6
# - -3 1 = -2
# + 1 1 = 2
n = int(input())
a = input()
c = [[None] * n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(i, n):
        if a[k] == "0":
            c[i][j] = 0
        elif a[k] == "-":
            c[i][j] = -1
        else:
            c[i][j] = 1

        k += 1


def check(numbers):
    m = len(numbers)

    for i in range(m):
        sn = 0

        for j in range(i, m):
            sn += numbers[j]

            if c[i][j] == 0 and sn != 0:
                return False
            elif c[i][j] == -1 and sn >= 0:
                return False
            elif c[i][j] == 1 and sn <= 0:
                return False

    return True


def go(index, numbers):
    if index == n:
        print(*numbers)
        exit()

    for i in range(-10, 11):
        if index != 0 and not check(numbers + [i]):
            continue

        go(index + 1, numbers + [i])


go(0, [])

