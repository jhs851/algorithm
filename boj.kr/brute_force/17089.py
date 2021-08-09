n, m = map(int, input().split())
relation = [[False] * (n + 1) for _ in range(n + 1)]
friends_counts = [0] * (n + 1)
answer = -1

for _ in range(m):
    v1, v2 = map(int, input().split())
    relation[v1][v2] = relation[v2][v1] = True
    friends_counts[v1] += 1
    friends_counts[v2] += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if relation[i][j]:
            for k in range(1, n + 1):
                if relation[i][k] and relation[j][k]:
                    sum_friends = friends_counts[i] + friends_counts[j] + friends_counts[k] - 6

                    if answer == -1 or answer > sum_friends:
                        answer = sum_friends

print(answer)

# 5 6
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
# 4 5
# 2

# 7 4
# 2 1
# 3 6
# 5 1
# 1 7
# -1
