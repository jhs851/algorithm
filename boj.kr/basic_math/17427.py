# 1 N까지 돌면서 O(N)
#   2 i의 약수를 더한다 (ONlgN)
# 100만 * 루트100만 -> 100만 * 1000 -> 10억 불가능
# N이하의 자연수 중에서 i를 약수로 갖는 수의 개수는 N // i개 -> O(N)
n = int(input())
answer = 0

for i in range(1, n + 1):
    answer += (n // i) * i

print(answer)
