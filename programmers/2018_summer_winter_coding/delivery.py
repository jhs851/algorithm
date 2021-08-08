import sys
from collections import deque


def solution(N, road, K):
    visited = {i: 0 if i == 1 else sys.maxsize for i in range(1, N + 1)}
    nodes = {}
    queue = deque([1])

    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]

    while queue:
        cur_node = queue.popleft()

        for next_node, d in nodes[cur_node]:
            if visited[next_node] > visited[cur_node] + d:
                visited[next_node] = visited[cur_node] + d
                queue.append(next_node)

    return len([True for d in visited.values() if d <= K])


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))  # 4
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))  # 4
