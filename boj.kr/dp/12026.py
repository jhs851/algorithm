n = int(input())
s = input()
d = [-1] * n
d[0] = 0


def get_prev(x):
    if x == 'B':
        return 'J'
    elif x == 'O':
        return 'B'
    elif x == 'J':
        return 'O'


for i in range(1, n):
    now = s[i]
    prev = get_prev(now)

    for j in range(i):
        if d[j] == -1:
            continue

        if s[j] != prev:
            continue

        cost = d[j] + (i - j) * (i - j)
        if d[i] == -1 or d[i] > cost:
            d[i] = cost

print(d[n - 1])
