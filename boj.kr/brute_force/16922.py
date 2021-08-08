# I V X L
# II VI VV XI XV XX LI LV LX LL
n = int(input())
answer = set()

for i in range(n + 1):
    for v in range(n - i + 1):
        for x in range(n - i - v + 1):
            l = n - i - v - x
            answer.add(i + v * 5 + x * 10 + l * 50)

print(len(answer))

# 1 4
# 2 10
# 10 244
