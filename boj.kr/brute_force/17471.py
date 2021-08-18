import sys
from collections import defaultdict
from itertools import combinations

answer = -1
n = int(input())
peoples = list(map(int, input().split()))
graph = defaultdict(list)
case = {i for i in range(n)}

for i in range(n):
    m = list(map(int, sys.stdin.readline().split()))

    for j in range(m[0]):
        graph[i].append(m[1 + j] - 1)


def is_connected(zones):
    stack = [zones[0]]
    visited = [False] * n
    visited[zones[0]] = True

    while stack:
        cur_index = stack.pop()

        for next_index in graph[cur_index]:
            if not visited[next_index] and next_index in zones:
                visited[next_index] = True
                stack.append(next_index)

    return visited.count(True) == len(zones)


# 모든 경우의 수
# 선거구는 구역을 적어도 하나 포함해야 한다
for i in range(1, n):
    for a in map(list, combinations(range(n), i)):
        b = list(case.difference(a))

        # 1선거구, 2선거구 모두 연결되어 있는지
        if is_connected(a) and is_connected(b):
            # 연결이 되어있다면 1선거구와 2선거구의 인구 차이
            peoples_1 = sum([peoples[k] for k in a])
            peoples_2 = sum([peoples[k] for k in b])

            temp = abs(peoples_1 - peoples_2)

            if answer == -1 or answer > temp:
                answer = temp

print(answer)
