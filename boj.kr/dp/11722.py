# 1. 점화식 정의 -> n번째 수로 만들 수 있는 가장 긴 감소하는 부분 수열
# 2. 작은 문제 -> d[0<i]까지 a[0<i]가 a[i]보다 크다면 감소하는 부분 수열
# 3. 점화식 -> d[i] = a[i] < a[j] ? max(d[i], d[j] + 1)
# 4. 시간복잡도 O(N^2)
# 5. 코드
n = int(input())
a = list(map(int, input().split()))
d = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
