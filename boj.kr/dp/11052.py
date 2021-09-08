# 1. 점화식의 정의 -> d[n] = n개를 갖기 위해 지불해야하는 최대 금액
# 2. 문제를 작게 만드는 방법 =
#   -> 가장 마지막에 구매하는 카드팩은 N가지
#   -> n가지만큼 모든 경우의 수의 비용을 계산해야함
# 3. 점화식 d[i] = max(d[i], d[i - j] + a[j]) 1 <= j <= i
# 4. 시간복잡도 = O(N^2) = 1,000,000
# 5. 코드짜기
n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + a[j])

print(d[n])
