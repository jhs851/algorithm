n = int(input())
b = list(map(int, input().split()))
answer = -1

if n == 1:
    print(0)
    exit()

for o1 in range(-1, 2):
    for o2 in range(-1, 2):
        change = 0

        if o1 != 0:
            change += 1

        if o2 != 0:
            change += 1

        b0 = b[0] + o1
        diff = (b[1] + o2) - b0
        bn = b0 + diff
        ok = True

        for i in range(2, n):
            bn += diff

            if b[i] == bn:
                continue
            elif b[i] - 1 == bn or b[i] + 1 == bn:
                change += 1
            else:
                ok = False
                break

        if ok and (answer == -1 or answer > change):
            answer = change

print(answer)

# 4
# 24 21 14 10
# 3

# 2
# 5 5
# 0

# 3
# 14 5 1
# -1

# 5
# 1 3 6 9 12
# 1
