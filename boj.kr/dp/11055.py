n = int(input())
s = list(map(int, input().split()))
dp = [x for x in s]

for i in range(n):
    for j in range(i):
        if (s[i] > s[j] and dp[i] < s[i] + dp[j]):
            dp[i] = s[i] + dp[j]

print(max(dp))

# 10
# 1 100 2 50 60 3 5 6 7 8 = 113
# dp[0] = 1
# dp[1] = 101
# dp[2] = 3
# dp[3] = 53
# dp[4] = 113
# dp[5] = 6
# dp[6] = 11
# dp[7] = 17
# dp[8] = 24
# dp[9] = 32
# s[i] > s[j] -> dp[i] = s[i] + dp[j]

# 10
# 1 100 2 101 60 3 5 6 7 8 = 202
