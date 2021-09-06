import sys

s = 0
m = int(input())

for _ in range(m):
    a = sys.stdin.readline().split()

    if len(a) > 1:
        x = int(a[1]) - 1

    if a[0] == "add":
        s = s | (1 << x)
    elif a[0] == "remove":
        s = s & ~(1 << x)
    elif a[0] == "check":
        if s & (1 << x) == 0:
            print(0)
        else:
            print(1)
    elif a[0] == "toggle":
        s = s ^ (1 << x)
    elif a[0] == "all":
        s = (1 << 20) - 1
    else:
        s = 0

