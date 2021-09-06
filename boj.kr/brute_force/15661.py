n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def go(index, first, second):
    if index == n:
        if len(first) == 0 or len(second) == 0:
            return -1

        t1 = 0
        t2 = 0

        for p1 in first:
            for p2 in first:
                if p1 == p2:
                    continue

                t1 += a[p1][p2]

        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue

                t2 += a[p1][p2]

        return abs(t1 - t2)

    answer = -1

    temp = go(index + 1, first + [index], second)
    if temp != -1:
        if answer == -1 or temp < answer:
            answer = temp

    temp = go(index + 1, first, second + [index])
    if temp != -1:
        if answer == -1 or temp < answer:
            answer = temp

    return answer


print(go(0, [], []))

