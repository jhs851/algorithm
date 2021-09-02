import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

answer = []


def go(x):
    visited[x] = True

    for next_student in graph[x]:
        if not visited[next_student]:
            go(next_student)

    answer.append(x)


for i in range(1, n + 1):
    if not visited[i]:
        go(i)

print(*answer)
