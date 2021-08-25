import sys

n, m = map(int, input().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
islands = [[0] * m for _ in range(n)]
islands_count = 0
bridges = [[0] * 7 for _ in range(7)]
costs = []

# 각 섬 표시
for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and islands[i][j] == 0:
            islands_count += 1
            stack = [(i, j)]
            islands[i][j] = islands_count

            while stack:
                x, y = stack.pop()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m:
                        if map[nx][ny] == 1 and islands[nx][ny] == 0:
                            stack.append((nx, ny))
                            islands[nx][ny] = islands_count

# 각 섬들과의 다리 길이
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            continue

        for k in range(4):
            distance = 0
            x, y = i + dx[k], j + dy[k]

            while 0 <= x < n and 0 <= y < m:
                if map[x][y] == 0:
                    pass
                elif islands[i][j] == islands[x][y]:
                    break
                else:
                    if distance >= 2:
                        island1 = islands[i][j]
                        island2 = islands[x][y]

                        if bridges[island1][island2] == 0 or bridges[island1][island2] > distance:
                            bridges[island1][island2] = distance
                            bridges[island2][island1] = distance
                    break

                x += dx[k]
                y += dy[k]
                distance += 1

# 다리 길이를 kruskal을 위해 1차원 배열로
for i in range(1, 7):
    for j in range(i + 1, 7):
        if bridges[i][j]:
            costs.append((i, j, bridges[i][j]))

if len(costs) == 0:
    print(-1)
    exit()

# kruskal
costs.sort(key=lambda item: item[2])
routes = {costs[0][0]}

while len(routes) != islands_count:
    for i, (i1, i2, cost) in enumerate(costs):
        if i1 in routes and i2 in routes:
            continue

        if i1 in routes or i2 in routes:
            routes.update([i1, i2])
            answer += cost
            costs.pop(i)
            break

print(answer)

# [0, 0, 0, 0, 0, 0, 1, 1],
# [2, 2, 0, 0, 0, 0, 1, 1],
# [2, 2, 0, 0, 0, 0, 0, 0],
# [2, 2, 0, 0, 0, 3, 3, 0],
# [0, 0, 0, 0, 0, 3, 3, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [4, 4, 4, 4, 4, 4, 4, 4]

# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 4, 0, 4, 0, 0],
# [0, 4, 0, 3, 2, 0, 0],
# [0, 0, 3, 0, 0, 0, 0],
# [0, 4, 2, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0]

# [(1, 2, 4), (1, 4, 4), (2, 3, 3), (2, 4, 2)]
