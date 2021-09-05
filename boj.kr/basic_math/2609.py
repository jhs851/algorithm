# 파이썬에 최대공약수를 구하는 패키지가 있지만 유클리드 호제법을 익힐겸 직접 구해보자


def gcd(x, y):
    if y == 0:
        return x

    return gcd(y, x % y)


a, b = map(int, input().split())
g = gcd(a, b)

print(g)
print(a * b // g)
