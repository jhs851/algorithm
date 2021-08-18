import sys
from itertools import combinations

n, m = map(int, input().split())
houses = []
chickens = []
city = [list(map(int, input().split())) for i in range(n)]
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j, sys.maxsize])
        elif city[i][j] == 2:
            chickens.append((i, j))

for case in combinations(chickens, m):
    _houses = [house[:] for house in houses]

    for i in range(len(_houses)):
        r1, c1, d = _houses[i]

        for r2, c2 in case:
            distance = abs(r1 - r2) + abs(c1 - c2)

            if d > distance:
                _houses[i][2] = distance
                d = distance

    sum_distance = sum([d for r, c, d in _houses])

    if answer > sum_distance:
        answer = sum_distance

print(answer)