# 1. 점화식 정의 -> d[i] = i일까지 벌 수 있는 최대 이익
# 2. 작은 문제 ->
# 3. 점화식 ->
# 4. 시간복잡도 ->
# 5. 코드
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [-1] * n


def go(day):
    if day == n:
        return 0

    if day > n:
        return -10**9

    if d[day] != -1:
        return d[day]

    t1 = go(day + a[day][0]) + a[day][1]
    t2 = go(day + 1)
    d[day] = max(t1, t2)

    return d[day]


print(go(0))
