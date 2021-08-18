a, b = map(int, input().split())


def go(number):
    if number == b:
        return 1

    if number > b:
        return -1

    r1 = go(number * 2)
    r2 = go(int(str(number) + "1"))

    if r1 == -1 and r2 == -1:
        return -1
    elif r1 == -1:
        return r2 + 1
    elif r2 == -1:
        return r1 + 1

    return min(r1, r2) + 1


print(go(a))