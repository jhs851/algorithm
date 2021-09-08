# 1. 점화식 정의
#   -> d1[i] = i번째에서 끝나는 최대 연속합
#   -> d2[i] = i번째에서 시작하는 최대 연속합
# 2. 작은문제 -> i번째 수를 제거한다면 연속합은 d1[i-1] + d2[i+1]
# 3. 점화식 -> max(max(d1), d1[i-1] + d2[i+1])
# 4. 시간복잡도 -> O(N)
# 5. 코드
n = int(input())
a = list(map(int, input().split()))
d1 = [0] * n
d2 = [0] * n

for i in range(n):
    d1[i] = a[i]

    if i == 0:
        continue

    if d1[i - 1] + a[i] > d1[i]:
        d1[i] = d1[i - 1] + a[i]

for i in range(n - 1, -1, -1):
    d2[i] = a[i]

    if i == n - 1:
        continue

    if d2[i + 1] + a[i] > d2[i]:
        d2[i] = d2[i + 1] + a[i]

answer = max(d1)

for i in range(1, n - 1):
    answer = max(answer, d1[i - 1] + d2[i + 1])

print(answer)

