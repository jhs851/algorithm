# 1. 점화식 정의 -> n번째까지의 증가 부분 수열 중 가장 합이 가장 큰 것
# 2. 작은 문제
#   -> d[i]와 d[i-1까지의] + a[i] 증가 부분 수열 합을 비교
# 3. 점화식 -> d[i] = a[i] > a[j] ? max(d[i], d[j] + a[i]) 0 <= j < i
# 4. 시간복잡도 O(N^2)
# 5. 코드
n = int(input())
a = list(map(int, input().split()))
d = a[::]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + a[i]:
            d[i] = d[j] + a[i]

print(d)
