# 9명 중에 2명을 고른다 O(N^2)
# 나머지 7명의 키에 합이 100인지 확인한다 O(N)
# O(N^3)
# 키의 합을 구해 놓고 s - a[i] - a[j] 가 100인지 확인할 수 있다
# O(N^2)
n = 9
a = sorted([int(input()) for _ in range(n)])
s = sum(a)

for l1 in range(n):
    for l2 in range(l1 + 1, n):
        if s - a[l1] - a[l2] == 100:
            for i in range(n):
                if i == l1 or i == l2:
                    continue

                print(a[i])

            exit()
