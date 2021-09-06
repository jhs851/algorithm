n, s = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

for i in range(1, 1 << n):
    sum = 0

    for k in range(n):
        if i & (1 << k):
            sum += a[k]

    if s == sum:
        answer += 1

print(answer)