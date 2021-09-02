# 각 카드의 크기를 구하고,
# 해당 카드 안에 다른 카드가 있을 때 그래프에 추가
from heapq import heappush, heappop

answer = ""
n, m = map(int, input().split())
grid = [input() for _ in range(n)]
cards_count = 0
graph = {}
ind = {}

for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            if grid[i][j] not in graph:
                graph[grid[i][j]] = []
                cards_count += 1

for card in graph.keys():
    ind[card] = 0

for card in graph.keys():
    minx = n - 1
    maxx = 0
    miny = m - 1
    maxy = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == card:
                minx = min(minx, i)
                maxx = max(maxx, i)
                miny = min(miny, j)
                maxy = max(maxy, j)

    for i in range(minx, maxx + 1):
        for j in range(miny, maxy + 1):
            if grid[i][j] == ".":
                print(-1)
                exit()

            if grid[i][j] != card and grid[i][j] not in graph[card]:
                graph[card].append(grid[i][j])
                ind[grid[i][j]] += 1

queue = []

for key, value in ind.items():
    if value == 0:
        heappush(queue, key)

while queue:
    cur_card = heappop(queue)

    answer += cur_card

    for next_card in graph[cur_card]:
        ind[next_card] -= 1

        if ind[next_card] == 0:
            heappush(queue, next_card)

if cards_count != len(answer):
    print(-1)
else:
    print(answer)
