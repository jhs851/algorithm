import sys
from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
ind = [0] * (n + 1)
hours = [0] * (n + 1)
answer = [0] * (n + 1)

for i in range(1, n + 1):
    work = list(map(int, sys.stdin.readline().split()))
    hours[i] = work[0]

    for x in work[2:]:
        graph[x].append(i)
        ind[i] += 1

queue = deque()

for i in range(1, n + 1):
    if ind[i] == 0:
        queue.append(i)
        answer[i] = hours[i]

while queue:
    cur_work = queue.popleft()

    for next_work in graph[cur_work]:
        ind[next_work] -= 1

        if answer[next_work] < answer[cur_work] + hours[next_work]:
            answer[next_work] = answer[cur_work] + hours[next_work]

        if ind[next_work] == 0:
            queue.append(next_work)

print(max(answer[1:]))
