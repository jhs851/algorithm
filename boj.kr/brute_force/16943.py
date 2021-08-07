from itertools import permutations

a, b = input().split()
answer = -1

for case in map(int, map("".join, permutations(a, len(a)))):
    if int(b) >= case > answer and len(str(case)) == len(a):
        answer = case

print(answer)
# 1234 3456  3421
# 1000 5  -1
# 789 123  -1
