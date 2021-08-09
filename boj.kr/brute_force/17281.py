from itertools import permutations

answer = 0
n = int(input())
players = [list(map(int, input().split())) for _ in range(n)]

for case in permutations([i for i in range(1, 9)], 8):
    score = 0
    _players = list(case[:3]) + [0] + list(case[3:])
    cur_index = 0

    for i in range(n):
        b1, b2, b3 = 0, 0, 0
        out_count = 0

        while out_count < 3:
            if players[i][_players[cur_index]] == 0:
                out_count += 1
            elif players[i][_players[cur_index]] == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif players[i][_players[cur_index]] == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif players[i][_players[cur_index]] == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            else:
                score += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0, 0

            cur_index += 1

            if cur_index > 8:
                cur_index = 0

    answer = max(answer, score)

print(answer)

# 2
# 4 0 0 0 0 0 0 0 0
# 4 0 0 0 0 0 0 0 0
# 1

# 2
# 4 0 0 0 1 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 4

# 2
# 0 4 4 4 4 4 4 4 4
# 0 4 4 4 4 4 4 4 4
# 43

# 2
# 4 3 2 1 0 4 3 2 1
# 1 2 3 4 1 2 3 4 0
# 46

# 9
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 4 4 4 4 4 4 4 4 0
# 216

# 9
# 1 2 4 3 0 2 1 0 3
# 1 2 1 2 0 0 0 0 1
# 3 4 2 3 1 2 3 4 0
# 0 1 2 3 4 2 1 0 0
# 0 0 0 0 0 0 1 4 4
# 0 4 0 4 0 4 0 4 0
# 0 4 2 2 2 2 2 2 2
# 1 1 1 1 1 1 1 1 0
# 0 2 0 3 0 1 0 2 0
# 89

