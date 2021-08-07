def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for time in times:
            count += mid // time

        if count >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer