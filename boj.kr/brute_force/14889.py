n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def go(index, first, second):
    if index == n:
        if len(first) != n // 2 or len(second) != n // 2:
            return -1

        t1 = 0
        t2 = 0

        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                t1 += a[first[i]][first[j]]
                t2 += a[second[i]][second[j]]

        return abs(t1 - t2)

    # 백트래킹
    if len(first) > n // 2 or len(second) > n // 2:
        return -1

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

