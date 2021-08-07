n = int(input())
bags = 0

while True:
    if n % 5 == 0:
        print(n // 5 + bags)
        break

    n -= 3
    bags += 1

    if n < 0:
        print(-1)
        break
