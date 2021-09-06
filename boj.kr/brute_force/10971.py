# 0 -> 1 -> 2 -> 3 -> 0
#   10   9   12    8
# 0 -> 1 -> 3 -> 2 -> 0
#   10   10    9    6

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


answer = -1
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
o = list(range(n))

while True:
    ok = True
    temp = 0

    for i in range(1, n):
        # 길이 없는 경우
        if a[o[i - 1]][o[i]] == 0:
            ok = False
            break

        temp += a[o[i - 1]][o[i]]

    if ok and a[o[-1]][o[0]] != 0:
        temp += a[o[-1]][o[0]]

        if answer == -1 or answer > temp:
            answer = temp

    if not next_permutation(o):
        break

    if o[0] != 0:
        break

print(answer)
