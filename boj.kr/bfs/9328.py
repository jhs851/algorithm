from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())

for _ in range(t):
    answer = 0
    h, w = map(int, input().split())
    a = ["*." + input() + ".*" for _ in range(h)]
    h += 4
    w += 4
    a = ["*" * w] + ["*" + ("." * (w - 2)) + "*"] + a + ["*" + ("." * (w - 2)) + "*"] + ["*" * w]
    keys = set(input())
    queue = deque([(1, 1)])
    doors = [[] for _ in range(26)]
    visited = [[False] * w for _ in range(h)]
    visited[1][1] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny]:
                    visited[nx][ny] = True

                    if a[nx][ny] == ".":
                        queue.append((nx, ny))
                    elif a[nx][ny] == "$":
                        queue.append((nx, ny))
                        answer += 1
                    elif 'a' <= a[nx][ny] <= 'z':
                        queue.append((nx, ny))

                        if a[nx][ny] not in keys:
                            keys.add(a[nx][ny])
                            queue.extend(doors[ord(a[nx][ny]) - ord('a')])
                    elif 'A' <= a[nx][ny] <= 'Z':
                        if a[nx][ny].lower() in keys:
                            queue.append((nx, ny))
                        else:
                            doors[ord(a[nx][ny]) - ord('A')].append((nx, ny))

    print(answer)
