# N * M번씩 최대 N * M 탐색
# NM^2 -> 250000^2 = 62,500,000,000 이걸론 안됨

# 첫번 째 칸이 나갈 수 있다면 지나가는 칸은 모두 나갈 수 있는 칸으로 표시
# 나갈 수 없다면 나갈 수 없는 칸으로 표시
# 표시가 되있다면 무시
# 표시가 없다면 체크
answer = 0
n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[None] * m for _ in range(n)]


def go(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return True
    elif check[r][c] is not None:
        return check[r][c]

    check[r][c] = False

    if a[r][c] == "U":
        check[r][c] = go(r - 1, c)
    elif a[r][c] == "R":
        check[r][c] = go(r, c + 1)
    elif a[r][c] == "D":
        check[r][c] = go(r + 1, c)
    else:
        check[r][c] = go(r, c - 1)

    return check[r][c]


for i in range(n):
    for j in range(m):
        if check[i][j] is None:
            go(i, j)

for i in range(n):
    for j in range(m):
        if check[i][j]:
            answer += 1

print(answer)
