n = int(input())
memo = [0] * (n + 1)
memo[1] = 9

for i in range(2, n + 1):
    memo[i] = memo[i - 1] * 2 - 1

print(memo[n])
