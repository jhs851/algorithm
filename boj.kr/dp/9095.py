# 1. 점화식의 정의 d[n] -> n을 1, 2, 3의 합으로 나타내는 방법의 수
# 2. 문제를 작게 만드는 방법
#   -> n은 맨 뒤에 1이나 2나 3이 들어 갈 수 있다.
#   -> 1을 넣었다면 n-1의 경우의 수와 같다
#   -> 2를 넣었다면 n-2의 경우의 수와 같다
#   -> 3을 넣었다면 n-3의 경우의 수와 같다
# 3. 점화식 -> d[n] = d[n - 1] + d[n - 2] + d[n - 3]
# 4. 시간복잡도 -> O(N) = 11
# 5. 코드짜기
t = int(input())

for _ in range(t):
    n = int(input())
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    for i in range(4, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    print(memo[n])

