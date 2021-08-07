t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    y, x = divmod(n, h)

    if x == 0:
        print(str(h) + str(y).zfill(2))
    else:
        print(str(x) + str(y + 1).zfill(2))

# 6 12 10  402
# 30 50 72  1203
# 2 2 4 202
# 5 100 45 509
