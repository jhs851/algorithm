answer = 0
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

for r1 in range(n):
    for c1 in range(m):
        if grid[r1][c1] == "#":
            _grid = [row[:] for row in grid]
            s1 = 0

            while True:
                if r1 + s1 >= n or r1 - s1 < 0 or c1 + s1 >= m or c1 - s1 < 0:
                    break
                elif _grid[r1 + s1][c1] != "#" or _grid[r1 - s1][c1] != "#" or _grid[r1][c1 + s1] != "#" or _grid[r1][c1 - s1] != "#":
                    break

                for i in range(s1 + 1):
                    _grid[r1 + i][c1] = "*"
                    _grid[r1 - i][c1] = "*"
                    _grid[r1][c1 + i] = "*"
                    _grid[r1][c1 - i] = "*"

                for r2 in range(n):
                    for c2 in range(m):
                        if grid[r2][c2] == "#":
                            s2 = 0

                            while True:
                                if r2 + s2 >= n or r2 - s2 < 0 or c2 + s2 >= m or c2 - s2 < 0:
                                    break
                                elif _grid[r2 + s2][c2] != "#" or _grid[r2 - s2][c2] != "#" or _grid[r2][c2 + s2] != "#" or _grid[r2][c2 - s2] != "#":
                                    break

                                answer = max(answer, (s1 * 4 + 1) * (s2 * 4 + 1))
                                s2 += 1

                s1 += 1

print(answer)

