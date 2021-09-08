# 1. 점화식의 정이 -> d[i] = i에 대한 제곱수 항의 최소 개수
# 2. 작은 문제
#    -> i의 마지막 항에 어떤 값(j)을 넣을지가 중요
#    -> d[i]에 마지막 항에 j^2을 넣었다면 마지막 항을 제외한 최소 개수는 d[i - j^2]
# 3. 점화식 -> d[i] = min(d[i - j^k]) + 1
# 4. 시간복잡도 -> O(N루트N)
# 5. 코드
n = int(input())
d = [i for i in range(n + 1)]

for i in range(2, n + 1):
    j = 1

    while j * j <= i:
        d[i] = min(d[i], d[i - j * j] + 1)
        j += 1

print(d[n])
# 1 = 1^2 -> 1
# 2 = 1^2 + 1^2 -> 2
# 3 = 1^2 + 1^2 + 1^2 -> 3
# 4 = 2^2 -> 1
# 5 = 2^2 + 1^2 -> 2
# 6 = 2^2 + 1^2 + 1^2 -> 3
# 7 = 2^2 + 1^2 + 1^2 + 1^2 -> 4
# 8 = 2^2 + 2^2 -> 2
# 9 = 3^3 -> 1
# 10 = 3^3 + 1^2 -> 2
# 11 = 3^3 + 1^2 + 1^2 -> 3
