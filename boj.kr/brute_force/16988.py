from collections import deque


def get_groups(a):
    n, m = len(a), len(a[0])
    d_r = [-1, 0, 1, 0]
    d_c = [0, -1, 0, 1]
    _a = [row[:] for row in a]
    groups = []

    for r in range(n):
        for c in range(m):
            group = []

            if _a[r][c] == 2:
                queue = deque([(r, c)])
                group.append((r, c))
                _a[r][c] = 1

                while queue:
                    _r, _c = queue.popleft()

                    for i in range(4):
                        new_r, new_c = _r + d_r[i], _c + d_c[i]

                        if not 0 <= new_r < n or not 0 <= new_c < m:
                            continue
                        elif _a[new_r][new_c] == 2:
                            queue.append((new_r, new_c))
                            group.append((new_r, new_c))
                            _a[new_r][new_c] = 1

            if group:
                groups.append(group)

    return groups


def solution():
    answer = 0
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    groups = get_groups(a)

    if not groups:
        return 0

    for r1 in range(n):
        for c1 in range(m):
            if a[r1][c1] != 0:
                continue

            _a = [row[:] for row in a]
            _a[r1][c1] = 1

            for r2 in range(n):
                for c2 in range(m):
                    if _a[r2][c2] != 0:
                        continue

                    _a[r2][c2] = 1
                    killed = 0

                    for group in groups:
                        for r, c in group:
                            if (r - 1 >= 0 and _a[r - 1][c] == 0) or (r + 1 < n and _a[r + 1][c] == 0) or (
                                    c - 1 >= 0 and _a[r][c - 1] == 0) or (c + 1 < m and _a[r][c + 1] == 0):
                                break
                        else:
                            killed += len(group)

                    answer = max(answer, killed)
                    _a[r2][c2] = 0

    return answer

print(solution())
