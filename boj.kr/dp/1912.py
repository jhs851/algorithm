# 1. 점화식 정의 -> d[i] = i번째 수로 끝나는 가장 큰 연속합
# 2. 작은 문제
# 3. 점화식 -> d[i] = d[i - 1] + a[i] >= a[i] ? d[i - 1] + a[i] : a[i]
# 4. 시간복잡도 -> O(N)
# 5. 코드
n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d[0] = a[0]

for i in range(1, n):
    if d[i - 1] + a[i] >= a[i]:
        d[i] = d[i - 1] + a[i]
    else:
        d[i] = a[i]

print(max(d))
