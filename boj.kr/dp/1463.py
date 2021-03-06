# d[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#      0  1  1  2  3  2  3  3  2  3
# 1. 점화식의 정의 -> d[n] = 연산을 사용하는 횟수
# 2. 문제를 작게 만들 수 있는 방법 찾기
#   -> n은 n/3, n/2, n-1중에 최소값 + 1
# 3. 점화식 만들기 -> d[n] = min(d[n-1], d[n/3], d[n/3]) + 1
# 4. 시간복잡도 계산해보기 O(N) * O(1) = 1,000,000
# 5. 코드짜기
n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])
