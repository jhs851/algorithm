n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]


def go(r, c, k):
    if r == n - 1 and c == n - 1:
        return 1

    answer = 0

    if k == 0:
        if c + 1 < n and house[r][c + 1] == 0:
            answer += go(r, c + 1, 0)
        if r + 1 < n and c + 1 < n and house[r + 1][c + 1] == 0 and house[r][c + 1] == 0 and house[r + 1][c] == 0:
            answer += go(r + 1, c + 1, 2)
    elif k == 1:
        if r + 1 < n and house[r + 1][c] == 0:
            answer += go(r + 1, c, 1)
        if r + 1 < n and c + 1 < n and house[r + 1][c + 1] == 0 and house[r][c + 1] == 0 and house[r + 1][c] == 0:
            answer += go(r + 1, c + 1, 2)
    else:
        if c + 1 < n and house[r][c + 1] == 0:
            answer += go(r, c + 1, 0)
        if r + 1 < n and house[r + 1][c] == 0:
            answer += go(r + 1, c, 1)
        if r + 1 < n and c + 1 < n and house[r + 1][c + 1] == 0 and house[r][c + 1] == 0 and house[r + 1][c] == 0:
            answer += go(r + 1, c + 1, 2)

    return answer


print(go(0, 1, 0))
