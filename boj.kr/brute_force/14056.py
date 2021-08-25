s = input()
k = int(input())

d = ["()"]
for l in range(4, len(s) + 1, 2):
    for i in range(len(d)):
        cur = d[i]

        if (l - 2) % len(cur) == 0:
            d.append("(" + (cur * ((l - 2) // len(cur))) + ")")

print(d)
