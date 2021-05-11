alpabet = ("", "a", "b", "c", "d", "e", "f", "g", "h")
input = input()
x, y = [alpabet.index(input[0]), int(input[1])]
result = 0

if x > 2 and y > 1:
    result += 1

if x > 2 and y > 2:
    result += 1

if x < 8 and y > 2:
    result += 1

if x < 7 and y > 1:
    result += 1

if x < 7 and y < 8:
    result += 1

if x < 8 and y < 7:
    result += 1

if x > 1 and y < 7:
    result += 1

if x > 2 and y < 8:
    result += 1

print(result)

# 답안
row = int(input[1])
column = int(ord(input[0])) - int(ord('a')) + 1
result = 0

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = ((-1, -2), (-2, -1), (-2, 1), (-1, 2),
         (1, 2), (2, 1), (2, -1), (1, -2))

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if (next_row > 0 and next_row < 9 and next_column > 0 and next_column < 9):
        result += 1

print(result)
