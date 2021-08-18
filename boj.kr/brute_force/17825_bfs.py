from collections import deque

answer = 0
dices = list(map(int, input().split()))
n = 33
a = [[i, i] for i in range(1, n + 1)]
a[5] = [22, 6]
a[10] = [28, 11]
a[15] = [30, 16]
a[21] = [21, 21]
a[27] = [20, 20]
a[29] = [25, 25]
a[32] = [25, 25]
score = [
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
    20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
    40, 0, 13, 16, 19, 25, 30, 35, 22, 24,
    28, 27, 26
]
queue = deque([(0, [0, 0, 0, 0], 0)])

while queue:
    index, horses, sum = queue.popleft()

    if index == len(dices):
        if sum > answer:
            answer = sum
        continue

    for i in range(4):
        location = horses[i]
        has_other_horse = False

        for j in range(dices[index]):
            location = a[location][0] if j == 0 else a[location][1]

        if location != 21:
            for j in range(4):
                if i != j and horses[j] == location:
                    has_other_horse = True

        if not has_other_horse:
            new_horses = horses[:]
            new_horses[i] = location
            queue.append((index + 1, new_horses, sum + score[location]))

print(answer)