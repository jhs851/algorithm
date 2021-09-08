# 1. 점화식의 정의 > d[n] = 길이가 N인 계단 수
# 2. 작은 문제
#   -> 길이가 N이면 이전에 사용한 수를 뺀 9개의 계단수를 추가할 수 있음
#   -> d[i][j] = i번째 계단 수, j 이전에 사용한 수
# 3. 점화식
#    d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
#    j == 0: d[i][j] = d[i - 1][1]
#    j == 9: d[i][j] = d[i - 1][8]
# 4. 시간복잡도 O(N) = 100
# 5. 코드
n = int(input())
d = [[1] * 10 for _ in range(n + 1)]
d[1][0] = 0
MOD = 1000000000

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][1] % MOD
        elif j == 9:
            d[i][j] = d[i - 1][8] % MOD
        else:
            d[i][j] = (d[i - 1][j - 1] + d[i - 1][j + 1]) % MOD

print(sum(d[n]) % MOD)
