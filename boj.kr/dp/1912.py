n = int(input())
dp = [0 for _ in range(n)]
s = list(map(int, input().split()))

dp[0] = s[0]

for i in range(1, n):
    dp[i] = dp[i - 1] + s[i] if dp[i - 1] + s[i] > s[i] else s[i]

print(max(dp))

# dp[i] = dp[i - 1] + s[i] > s[i] ? dp[i - 1] + s[i] > s[i]
# 10 -4 3 1 5 6 -35 12 21 -1 = 33
# dp[0] = 10
# dp[1] = 6
# dp[2] = 9
# dp[3] = 10
# dp[4] = 15
# dp[5] = 21
# dp[6] = -14
# dp[7] = 12
# dp[8] = 33
# dp[9] = 32

# 2 1 -4 3 4 -4 6 5 -5 1 = 14
# dp[0] = 2
# dp[1] = 3
# dp[2] = -1
# dp[3] = 3
# dp[4] = 7
# dp[5] = 3
# dp[6] = 9
# dp[7] = 14
# dp[8] = 9
# dp[9] = 10

# -1 -2 -3 -4 -5 = -1
# dp[0] = -1
# dp[1] = -2
# dp[2] = -3
# dp[3] = -4
# dp[4] = -5
