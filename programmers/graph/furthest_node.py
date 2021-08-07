import heapq
import sys
from collections import defaultdict, Counter


def solution(n, edge):
    answer = {i: 0 if i == 1 else sys.maxsize for i in range(1, n + 1)}
    nodes = defaultdict(list)
    queue = []
    heapq.heappush(queue, (0, 1))

    for v1, v2 in edge:
        nodes[v1].append((v2, 1))
        nodes[v2].append((v1, 1))

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if cur_distance > answer[cur_node]:
            continue

        for next_node, next_distance in nodes[cur_node]:
            if answer[next_node] > answer[cur_node] + next_distance:
                answer[next_node] = answer[cur_node] + next_distance
                heapq.heappush(queue, (answer[next_node], next_node))

    return Counter(answer.values())[max(answer.values())]


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3
