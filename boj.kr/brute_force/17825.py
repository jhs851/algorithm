dices = list(map(int, input().split()))
n = 33
a = [[i, i] for i in range(1, n + 1)]
a[5] = [22, 6]
a[10] = [28, 11]
a[15] = [30, 16]
a[21] = [21, 21]
a[27] = [20, 20]
a[29] = [25, 25]
a[32] = [25, 25]
score = [
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
    20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
    40, 0, 13, 16, 19, 25, 30, 35, 22, 24,
    28, 27, 26
]


def get_next(horse, distance):
    next = horse

    for i in range(distance):
        next = a[next][0] if i == 0 else a[next][1]

    return next


def go(index, horses, sum_score):
    if index == len(dices):
        return sum_score

    answer = 0

    for i in range(4):
        next = get_next(horses[i], dices[index])
        ok = True

        if next != 21:
            for j in range(4):
                if i == j:
                    continue
                if horses[j] == next:
                    ok = False

        if ok:
            _horses = horses[:]
            _horses[i] = next
            temp = go(index + 1, _horses, sum_score + score[next])

            if temp > answer:
                answer = temp

    return answer


print(go(0, [0, 0, 0, 0], 0))
