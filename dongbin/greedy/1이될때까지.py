# 시간 복잡도 O(logN)

n, k = map(int, input().split())
count = 0

while (n > 1):
    if (n % k == 0):
        n = n // k
    else:
        n -= 1

    count += 1

print(count)

# 답안
result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
