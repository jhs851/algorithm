# 100만까지의 모든 소수들을 구한다. O(NlgN)
MAX = 1000000
p = []
c = [True] * (MAX + 1)
c[0] = False
c[1] = False

for i in range(2, MAX + 1):
    if c[i]:
        p.append(i)
        j = i * i

        while j <= MAX:
            c[j] = False
            j += i

answer = []
while True:
    n = int(input())

    if n == 0:
        break

    for i in range(1, len(p)):
        if c[n - p[i]]:
            answer.append("{0} = {1} + {2}".format(n, p[i], n - p[i]))
            break

print("\n".join(answer) + "\n")
