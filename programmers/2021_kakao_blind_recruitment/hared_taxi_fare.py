import sys
import heapq


def dikstra(s, e, n, nodes):
    costs = {i: 0 if i == s else sys.maxsize for i in range(1, n + 1)}
    queue = []
    heapq.heappush(queue, (costs[s], s))

    while queue:
        cur_costs, cur_node = heapq.heappop(queue)

        if costs[cur_node] < cur_costs:
            continue

        for next_node, cost in nodes[cur_node]:
            if costs[next_node] > costs[cur_node] + cost:
                costs[next_node] = costs[cur_node] + cost
                heapq.heappush(queue, (costs[next_node], next_node))

    return costs[e]


def solution(n, s, a, b, fares):
    answer = sys.maxsize
    nodes = {}

    for v1, v2, cost in fares:
        nodes[v1] = nodes.get(v1, []) + [(v2, cost)]
        nodes[v2] = nodes.get(v2, []) + [(v1, cost)]

    for i in range(1, n + 1):
        if i in nodes:
            costs = dikstra(s, i, n, nodes) + dikstra(i, a, n, nodes) + dikstra(i, b, n, nodes)

            if answer > costs:
                answer = costs

    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6,
               [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18
