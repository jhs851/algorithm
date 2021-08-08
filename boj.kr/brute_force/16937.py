h, w = map(int, input().split())
n = int(input())
r = [0] * n
c = [0] * n
answer = 0

for i in range(n):
    r[i], c[i] = map(int, input().split())

for i in range(n):
    r1, c1 = r[i], c[i]

    for j in range(i + 1, n):
        r2, c2 = r[j], c[j]

        for _ in range(2):
            for _ in range(2):
                if r1 + r2 <= h and max(c1, c2) <= w:
                    temp = r1 * c1 + r2 * c2

                    if answer < temp:
                        answer = temp

                if c1 + c2 <= w and max(r1, r2) <= h:
                    temp = r1 * c1 + r2 * c2

                    if answer < temp:
                        answer = temp

                r2, c2 = c2, r2

            r1, c1, = c1, r1

print(answer)

# 2 2
# 2
# 1 2
# 2 1
# 4

# 10 9
# 4
# 2 3
# 1 1
# 5 10
# 9 11
# 56

# 10 10
# 3
# 6 6
# 7 7
# 20 5
# 0
