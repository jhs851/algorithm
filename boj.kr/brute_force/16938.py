from itertools import combinations

n, l, r, x = map(int, input().split())
difficulties = list(map(int, input().split()))
answer = 0

for i in range(2, n + 1):
    for case in combinations(difficulties, i):
        if l <= sum(case) <= r and max(case) - min(case) >= x:
            answer += 1

print(answer)

# 3 5 6 1
# 1 2 3
# 2

# 4 40 50 10
# 10 20 30 25
# 2

# 5 25 35 10
# 10 10 20 10 20
# 6
