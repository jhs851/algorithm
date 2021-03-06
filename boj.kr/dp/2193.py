# 1. 점화식 정의 -> d[n] = N자리 이친수의 개수
# 2. 작은 문제
#   -> 이전 값이 1인지 아닌지 확인하고, 1이라면 0만 붙일 수 있고, 0이라면 0과 1 모두 붙일 수 있다.
#   -> d[i][j] = i는 i자리 이친수의 개수, j는 이전값이 0인지 1인지
# 3. 점화식
#    -> d[i][0] = d[i - 1][0] + d[i - 1][1]
#    -> d[i][1] = d[i - 1][0]
# 4. 시간복잡도 O(N) = 90
# 5. 코드
n = int(input())
d = [[0] * 2 for _ in range(n + 1)]
d[1][1] = 1

for i in range(2, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[n]))
