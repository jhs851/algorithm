import heapq
import sys
from collections import defaultdict

# 수빈이가 집에 가는 가장 빠른 시간을 출력
# 제일 처음에 수빈이의 위치는 (xs, ys)
# 집이 위치한 (xe, ye)로 이동
# 수빈이는 두 가지 방법으로 이동
# 1. 점프. 예를 들어 (x, y)에 있는 경우에 (x+1, y), (x-1, y), (x, y+1), (x, y-1)로 이동할 수 있다. 점프는 1초가 걸린다.
# 2. 텔레포트.
# 텔레포트를 할 수 있는 방법은 총 세 가지가 있으며, 미리 정해져 있다.
# 텔레포트는 네 좌표 (x1, y1), (x2, y2)로 나타낼 수 있으며, (x1, y1)에서 (x2, y2)로
# 또는 (x2, y2)에서 (x1, y1)로 이동할 수 있 다는 것이다.
# 텔레포트는 10초가 걸린다.
# 최단거리 문제, 다익스트라를 사용해보자

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
teleports = [list(map(int, sys.stdin.readline().split())) for i in range(3)]
distances = [0 if i == 0 else sys.maxsize for i in range(8)]
nodes = defaultdict(list)
nodes[0].append((1, abs(xs - xe) + abs(ys - ye)))
nodes[1].append((0, abs(xs - xe) + abs(ys - ye)))

for i, (x1, y1, x2, y2) in enumerate(teleports):
    t1 = (i + 1) * 2
    t2 = t1 + 1

    # 수빈
    nodes[0].append((t1, abs(xs - x1) + abs(ys - y1)))
    nodes[0].append((t2, abs(xs - x2) + abs(ys - y2)))
    # 집
    nodes[1].append((t1, abs(xe - x1) + abs(ye - y1)))
    nodes[1].append((t2, abs(xe - x2) + abs(ye - y2)))
    # 텔레포트
    nodes[t1].append((t2, 10))
    nodes[t1].append((0, abs(xs - x1) + abs(ys - y1)))
    nodes[t1].append((1, abs(xe - x1) + abs(ye - y1)))

    nodes[t2].append((t1, 10))
    nodes[t2].append((0, abs(xs - x2) + abs(ys - y2)))
    nodes[t2].append((1, abs(xe - x2) + abs(ye - y2)))

for i, (x1, y1, x2, y2) in enumerate(teleports):
    t1 = (i + 1) * 2
    t2 = t1 + 1

    for j, (xx1, yy1, xx2, yy2) in enumerate(teleports):
        t3 = (j + 1) * 2
        t4 = t3 + 1

        if i != j:
            nodes[t1].append((t3, abs(x1 - xx1) + abs(y1 - yy1)))
            nodes[t1].append((t4, abs(x1 - xx2) + abs(y1 - yy2)))
            nodes[t2].append((t3, abs(x2 - xx1) + abs(y2 - yy1)))
            nodes[t2].append((t4, abs(x2 - xx2) + abs(y2 - yy2)))

queue = []
heapq.heappush(queue, (distances[0], 0))

while queue:
    cur_distance, cur_node = heapq.heappop(queue)

    if cur_distance > distances[cur_node]:
        continue

    for next_node, next_distance in nodes[cur_node]:
        distance = distances[cur_node] + next_distance

        if distances[next_node] > distance:
            distances[next_node] = distance
            heapq.heappush(queue, (distance, next_node))

print(distances[1])
