# 교환은 O(N^2)
# 확인 O(N^2)
# O(N^4) = 6,250,000

n = int(input())
a = [list(input()) for _ in range(n)]
answer = 1


def check():
    global answer

    for i in range(n):
        count = 1

        for j in range(1, n):
            if a[i][j] == a[i][j - 1]:
                count += 1
            else:
                count = 1

            if count > answer:
                answer = count

        count = 1
        for j in range(1, n):
            if a[j][i] == a[j - 1][i]:
                count += 1
            else:
                count = 1

            if count > answer:
                answer = count


for i in range(n):
    for j in range(1, n):
        if a[i][j] != a[i][j - 1]:
            a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
            check()
            a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]

        if a[j][i] != a[j - 1][i]:
            a[j][i], a[j - 1][i] = a[j - 1][i], a[j][i]
            check()
            a[j][i], a[j - 1][i] = a[j - 1][i], a[j][i]

print(answer)
