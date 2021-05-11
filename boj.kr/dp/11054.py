n = int(input())
s = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if (s[i] > s[j] and dp[i] < dp[j]):
            dp[i] = dp[j]

    dp[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if (s[i] > s[j] and dp2[i] < dp2[j]):
            dp2[i] = dp2[j]

    dp2[i] += 1
    dp[i] += dp2[i] - 1

print(max(dp))

# 10
# 1 5 2 1 4 3 4 5 2 1 = 7

# dp[0] = 1
# dp[1] = 2
# dp[2] = 2
# dp[3] = 1
# dp[4] = 3
# dp[5] = 3
# dp[6] = 4
# dp[7] = 5
# dp[8] = 2
# dp[9] = 1

# dp[9] = 1
# dp[8] = 2
# dp[7] = 3
# dp[6] = 3
# dp[5] = 3
# dp[4] = 4
# dp[3] = 1
# dp[2] = 2
# dp[1] = 5
# dp[0] = 1

# s[i]가 s[이전 j들]의 값보다 클 때 -> dp[i] = s[i]가 s[이전 j들]의 값보다 크면서 가장 큰 dp[이전 j들]
# dp에는 +1씩
# 반대로 한번더, +1 안함
