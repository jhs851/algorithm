import sys

t = int(input())


def go(s, n):
    if s == n:
        return 1

    if s > n:
        return 0

    answer = 0

    for i in range(1, 4):
        answer += go(s + i, n)

    return answer


for _ in range(t):
    n = int(sys.stdin.readline())

    print(go(0, n))
