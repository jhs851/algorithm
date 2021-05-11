# 시간복잡도 O(N)

n = int(input())
directions = input().split()
result = [1, 1]

for direction in directions:
    if (direction == 'U' and result[0] > 1):
        result[0] -= 1
    elif (direction == 'D' and result[0] < n):
        result[0] += 1
    elif (direction == 'L' and result[1] > 1):
        result[1] -= 1
    elif (direction == 'R' and result[1] < n):
        result[1] += 1

print(result[0], result[1])

# 답안
x, y = 1, 1
# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for direction in directions:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if direction == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
