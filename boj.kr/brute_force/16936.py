n = int(input())
answer = list(map(int, input().split()))

for i in range(n):
    number = answer[i]
    count = 0

    while number % 3 == 0:
        number //= 3
        count += 1

    answer[i] = (-count, answer[i])

answer.sort()
answer = [number for count, number in answer]
print(*answer, sep=" ")
# 6
# 4 8 6 3 12 9
# 9 3 6 12 4 8
