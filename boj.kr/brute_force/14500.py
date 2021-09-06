n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if j + 3 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3]
            answer = max(answer, temp)

        if i + 3 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 3][j]
            answer = max(answer, temp)

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2]
            answer = max(answer, temp)

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 2][j]
            answer = max(answer, temp)

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 2]
            answer = max(answer, temp)

        if i + 2 < n and j - 1 >= 0:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j - 1]
            answer = max(answer, temp)

        if i - 1 >= 0 and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i - 1][j + 2]
            answer = max(answer, temp)

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j + 1]
            answer = max(answer, temp)

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j]
            answer = max(answer, temp)

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1]
            answer = max(answer, temp)

        if i + 1 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
            answer = max(answer, temp)

        if i - 1 >= 0 and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i - 1][j + 1] + a[i - 1][j + 2]
            answer = max(answer, temp)

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1]
            answer = max(answer, temp)

        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j + 2]
            answer = max(answer, temp)

        if i + 2 < n and j - 1 >= 0:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j - 1] + a[i + 2][j - 1]
            answer = max(answer, temp)

        if j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2]
            if i - 1 >= 0:
                temp2 = temp + a[i - 1][j + 1]
                answer = max(answer, temp2)

            if i + 1 < n:
                temp2 = temp + a[i + 1][j + 1]
                answer = max(answer, temp2)

        if i + 2 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j]
            if j + 1 < m:
                temp2 = temp + a[i + 1][j + 1]
                answer = max(answer, temp2)

            if j - 1 >= 0:
                temp2 = temp + a[i + 1][j - 1]
                answer = max(answer, temp2)

print(answer)
