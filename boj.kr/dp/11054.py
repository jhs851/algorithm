# 1. 점화식 정의 -> n번째에서 만들 수 있는 가장 긴 바이토닉 부분 수열의 길이
# 2. 작은문제
#   -> i번째까지 가장 긴 증가하는 부분 수열과 a를 반대로 했을 때 가장 긴 증가하는 부분 수열을 저장
# 3. 점화식
#   -> d[i][0] = a[i] > a[j] ? max(d[i][0], d[j][0] + 1)
#   -> d[i][1] = a[n - i] > a[n - j] ? max(d[n - i - 1][1], d[n - j - 1][1] + 1)
# 4. 시간복잡도 O(N^2)
# 5. 코드
n = int(input())
a = list(map(int, input().split()))
d = [[1] * 2 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i][0] = max(d[i][0], d[j][0] + 1)
        if a[n - i - 1] > a[n - j - 1]:
            d[n - i - 1][1] = max(d[n - i - 1][1], d[n - j - 1][1] + 1)

print(max(map(sum, d)) - 1)
