# n <= 100,000,000 이다
# 건너뛰어야 한다

n = int(input())
answer = 0
start = 1
len = 1

while start <= n:
    end = start * 10 - 1

    if end > n:
        end = n

    answer += (end - start + 1) * len
    start *= 10
    len += 1

print(answer)
