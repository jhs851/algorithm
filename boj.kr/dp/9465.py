T = int(input())

for i in range(T):
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(2)]
    st = [[0 for _ in range(n)] for _ in range(2)]

    for j in range(2):
        st[j] = list(map(int, input().split()))
        dp[j][0] = st[j][0]

    for j in range(1, n):
        dp[0][j] = st[0][j] + max(dp[1][j - 1], j > 1 and dp[1][j - 2])
        dp[1][j] = st[1][j] + max(dp[0][j - 1], j > 1 and dp[0][j - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))

# 50 10 100 20 40
# 30 50  70 10 60

# 50  40 200 140 250
# 30 100 120 210 260
