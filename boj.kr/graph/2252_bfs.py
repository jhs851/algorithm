import sys
from collections import deque, defaultdict

n, m = map(int, input().split())
ind = [0] * (n + 1)
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    ind[b] += 1

answer = []
queue = deque()

for i in range(1, n + 1):
    if ind[i] == 0:
        queue.append(i)

while queue:
    cur_student = queue.popleft()
    answer.append(cur_student)

    for next_student in graph[cur_student]:
        ind[next_student] -= 1

        if ind[next_student] == 0:
            queue.append(next_student)

print(*answer)
