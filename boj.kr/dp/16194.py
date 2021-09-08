# 11052 카드 구매하기 1과 매우 유사함
# 차이점은 최대값 -> 최소값
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = a[i]

    for j in range(1, i + 1):
        d[i] = min(d[i], d[i - j] + a[j])

print(d[n])
