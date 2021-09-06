def next_permutation(a):
    i, j = len(a) - 1, len(a) - 1

    while i > 0 and a[i - 1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    while a[i - 1] >= a[j]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = a[i:][::-1]

    return True


def check(a):
    sa = 0

    for i in range(1, len(a)):
        sa += abs(a[i - 1] - a[i])

    return sa


answer = 0
n = int(input())
a = sorted(list(map(int, input().split())))

while True:
    answer = max(answer, check(a))

    if not next_permutation(a):
        break

print(answer)