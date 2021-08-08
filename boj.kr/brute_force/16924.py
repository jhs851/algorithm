n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
check = [[True] * m for _ in range(n)]
answer = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == "*":
            check[i][j] = False

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if grid[i][j] == "*":
            l = 0
            k = 1

            while True:
                if 0 <= i - k and i + k < n and 0 <= j - k and j + k < m:
                    if grid[i - k][j] == "*" and grid[i + k][j] == "*" and grid[i][j - k] == "*" and grid[i][j + k] == "*":
                        l = k
                        k += 1
                    else:
                        break
                else:
                    break

            if l:
                answer.append((i + 1, j + 1, l))

                check[i][j] = True
                for k in range(1, l + 1):
                    check[i - k][j] = True
                    check[i + k][j] = True
                    check[i][j - k] = True
                    check[i][j + k] = True

for i in range(n):
    if False in check[i]:
        print(-1)
        break
else:
    print(len(answer))

    for r, c, l in answer:
        print(r, c, l)

# 6 8
# ....*...
# ...**...
# ..*****.
# ...**...
# ....*...
# ........
# 3
# 3 4 1
# 3 5 2
# 3 5 1

# 5 5
# .*...
# ****.
# .****
# ..**.
# .....
# 3
# 2 2 1
# 3 3 1
# 3 4 1

# 5 5
# .*...
# ***..
# .*...
# .*...
# .....
# -1
