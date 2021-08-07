n = int(input())
memo = [0] * (n + 1)
memo[1] = 1
memo[2] = 2

for i in range(3, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 10007

print(memo[n])

