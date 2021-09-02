from collections import deque

n, k = map(int, input().split())
MAX = 200000
visited = [False] * MAX
visited[n] = True
count = [0] * MAX
count[n] = 1
d = [0] * MAX
queue = deque([n])

while queue:
    x = queue.popleft()

    for nx in [x - 1, x + 1, x * 2]:
        if 0 <= nx < MAX:
            if not visited[nx]:
                visited[nx] = True
                d[nx] = d[x] + 1
                count[nx] = count[x]
                queue.append(nx)
            elif d[nx] == d[x] + 1:
                count[nx] += count[x]

print(d[k])
print(count[k])
