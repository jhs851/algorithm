# 에라토스테네스의 체 구현

n = 100
primes = []
check = [True] * (n + 1)
check[0] = False
check[1] = False

for i in range(2, n + 1):
    if check[i]:
        primes.append(i)
        j = i * i

        while j <= n:
            check[j] = False
            j += i

print(primes)
