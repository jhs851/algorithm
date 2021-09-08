# 11053과 유사한 문제
# 가장 긴 증가하는 수열을 출력해야함
# 이런식으로 문제의 답을 증명해야하는 경우 역추적으로 증명할 수 있다
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
v = [0] * (n + 1)
d[1] = 1
v[1] = 0

for i in range(2,  n + 1):
    for j in range(i - 1, 0, -1):
        if a[j] < a[i] and d[i] < d[j]:
            d[i] = d[j]
            v[i] = j

    d[i] += 1

md = max(d)
mi = d.index(md)
s = []

for _ in range(md):
    s.append(a[mi])
    mi = v[mi]

print(md)
print(*s[::-1])
