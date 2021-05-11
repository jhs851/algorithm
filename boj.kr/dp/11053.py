n = int(input())
dp = [0 for _ in range(n)]
s = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if (s[i] > s[j] and dp[i] < dp[j]):
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))

# s[이전의 i]들 중에 s[i]보다 작은 s[이전의 i]가 있다면 dp[i] = 1 + s[i]보다 작은 s[이전의 i]들 중 가장 큰 dp[i]

# dp[0] = 1
# dp[1] = 2
# dp[2] = 1
# dp[3] = 3
# dp[4] = 2
# dp[5] = 4
# [10, 20, 10, 30, 20, 50] = 4

# dp[0] = 1
# dp[1] = 2
# dp[2] = 1
# dp[3] = 2
# dp[4] = 3
# dp[5] = 4
# [10, 30, 10, 20, 30, 50] = 4

# dp[0] = 1
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 2
# dp[5] = 1
# [60, 10, 30, 70, 20, 10] = 3
