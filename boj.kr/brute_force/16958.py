import sys

n, t = map(int, input().split())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = int(input())
ab = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
specials = [(x, y) for s, x, y in cities if s == 1]

for a, b in ab:
    s1, x1, y1 = cities[a - 1]
    s2, x2, y2 = cities[b - 1]

    # A -> B
    distance = abs(x1 - x2) + abs(y1 - y2)

    # A -> A에서 가장 가까운 특별한 도시(A포함) -> B에서 가장 가까운 특별한 도시(B포함) -> B
    a_nearest = sys.maxsize
    b_nearest = sys.maxsize
    for x, y in specials:
        a_nearest = min(a_nearest, abs(x1 - x) + abs(y1 - y))
        b_nearest = min(b_nearest, abs(x2 - x) + abs(y2 - y))

    print(min(distance, a_nearest + t + b_nearest))
