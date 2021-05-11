# 시간 복잡도 O(K)

N = int(input())
currencies = [500, 100, 50, 10]
count = 0

for currency in currencies:
    count += N // currency
    N %= currency

print(count)
