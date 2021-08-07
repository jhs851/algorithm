from collections import deque


def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [0] * n

    while 0 in visited:
        index = visited.index(0)
        queue.append(index)
        visited[index] = 1

        while queue:
            node = queue.popleft()

            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    queue.append(i)
                    visited[i] = 1

        answer += 1

    return answer