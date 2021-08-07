import math

a, b, v = map(int, input().split())

c = a - b
count = math.ceil(v // c)

if v <= c * (count - 1) + a:
    print(count - b)
else:
    print(count)

# 2 1 5 4
# 4 2 10 4
# 5 1 6 2
# 100 99 1000000000 999999901
