from collections import deque


def solution(prices):
    queue = deque(prices)
    result = []

    while queue:
        current_price = queue.popleft()
        count = 0

        for price in queue:
            count += 1

            if current_price > price:
                break

        result.append(count)

    return result


prices = list(map(int, input().split()))
print(solution(prices))

print("정답 = [2, 1, 2, 1, 0] / 현재 풀이 값 = ", solution([6, 9, 5, 7, 4]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", solution([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", solution([1, 5, 3, 6, 7, 6, 5]))
