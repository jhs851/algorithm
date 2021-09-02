from collections import deque

n, k = map(int, input().split())
a = [input() for _ in range(2)]
queue = deque([(0, 0)])
d = [[-1] * n for _ in range(2)]
d[0][0] = 0

while queue:
    i, j = queue.popleft()

    for ni, nj in ((i, j + 1), (i, j - 1), ((i + 1) % 2, j + k)):
        if nj >= 0:
            if nj >= n:
                print(1)
                exit()
            elif d[i][j] >= nj:
                continue
            elif a[ni][nj] == "1" and d[ni][nj] == -1:
                queue.append((ni, nj))
                d[ni][nj] = d[i][j] + 1

print(0)
