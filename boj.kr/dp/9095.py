t = int(input())

for _ in range(t):
    n = int(input())
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    for i in range(4, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    print(memo[n])

