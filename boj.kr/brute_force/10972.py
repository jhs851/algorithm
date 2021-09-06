def next_permutation(a):
    n = len(a)
    i = n - 1

    while i > 0 and a[i - 1] >= a[i]:
        i -= 1

    if i <= 0:
        return False

    j = n - 1

    while a[i - 1] >= a[j]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = a[i:][::-1]

    return True


n = int(input())
a = list(map(int, input().split()))
if not next_permutation(a):
    print(-1)
else:
    print(*a)
