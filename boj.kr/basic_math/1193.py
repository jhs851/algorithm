x = int(input())
answer = []

# 몇번 째 라인이냐
line = 1
max_number = 1
while max_number < x:
    line += 1
    max_number += line

answer = [1, line]

for _ in range(max_number - x):
    answer[0] += 1
    answer[1] -= 1

if line % 2 == 0:
    answer.reverse()

print("/".join(map(str, answer)))
