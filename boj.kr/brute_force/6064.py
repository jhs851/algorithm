t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    for i in range(x, m * n + 1, m):
        if i % n == y:
            print(i + 1)
            break
    else:
        print(-1)
