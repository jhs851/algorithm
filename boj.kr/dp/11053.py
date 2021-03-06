# 1. 점화식의 정의 -> d[n] = n까지의 가장 긴 증가하는 부분 수열의 길이
# 2. 작은 문제
#    -> d의 i는 i까지 가장 긴 증가하는 부분 수열의 길이
#    -> j를 i - 1부터 -1씩 감소하며 a[j] 가 a[i] 보다 작다면 d[i] = d[j] + 1
# 3. 점화식
# 4. 시간복잡도 O(N^2) = 1,000,000
# 5. 코드
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
d[1] = 1

for i in range(2,  n + 1):
    for j in range(i - 1, 0, -1):
        if a[j] < a[i] and d[i] < d[j]:
            d[i] = d[j]

    d[i] += 1

print(max(d))
# 10 20 10 30 20 50 = 4
# 10 30 10 20 30 50 = 4
# 60 10 30 70 20 10 = 3
# 60 10 30 70 40 50 = 4
