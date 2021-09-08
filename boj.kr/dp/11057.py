# 1. 점화식 정의 -> 수의 길이 N으로 만들 수 있는 오르막 수의 개수
# 2. 작은 문제
#   -> 이전 값을 저장해둔다면 이전값보다 같거나 크고 10보다 작은 수들의 수를 저장해놓는다
#   -> d[i][j] = i길이의 이전값이 j인 오르막 수
# 3. 점화식 -> d[i][j] = d[i - 1][j < 10]
# 4. 시간복잡도(문제의수 * 풀이복잡도) -> O(N)
# 5. 코드
MOD = 10007
n = int(input())
d = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            d[i][j] += d[i - 1][k]
            d[i][j] %= MOD

print(sum(d[n]) % MOD)
