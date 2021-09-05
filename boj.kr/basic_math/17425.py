# 17427 문제와 비슷하지만 테스트 케스트의 제한이 10만이다
# O(TN) -> 10억이므로 불가능
# 테스트 케스트가 많은 경우는 값을 미리 모두 저장해놓는다 -> 입력에 따라 값이 바뀌지 않기 때문
# O(NlgN)
# d는 f(i)
# s는 g(i)
MAX = 1000000
d = [1] * (MAX + 1)
s = [0] * (MAX + 1)

for i in range(2, MAX + 1):
    j = 1

    while i * j <= MAX:
        d[i * j] += i
        j += 1

for i in range(1, MAX + 1):
    s[i] = s[i - 1] + d[i]

t = int(input())
answer = []

for _ in range(t):
    n = int(input())

    answer.append(str(s[n]))

print("\n".join(answer) + "\n")
