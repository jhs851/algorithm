n = int(input())
s = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if (s[i] > s[j] and dp[i] < dp[j]):
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))

# 6
# 10 30 10 20 20 10 = 3
# 11053 거꾸로
