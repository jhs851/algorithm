# 1. 점화식 정의 -> d[i] = i를 1, 2, 3의 합으로 나타내는 방법의 수
# 2. 작은 문제
#   -> d[i]에 1을 붙이면 d[i-1]의 경우의 수
#   -> d[i]에 2를 붙이면 d[i-2]의 경우의 수
#   -> d[i]에 3을 붙이면 d[i-3]의 경우의 수
# 3. 점화식 -> d[i] = d[i-1] + d[i-2] + d[i-3] + 1
# 4. 시간복잡도 O(N) = 1,000,000
# 5. 코드
import sys

MAX = 1000000
MOD = 1000000009
d = [0] * (MAX + 1)
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, MAX + 1):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % MOD

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(d[n])
