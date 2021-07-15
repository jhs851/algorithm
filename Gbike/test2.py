def solution(nums):
    unique = set(nums)

    return len(nums) // 2 if len(nums) // 2 < len(unique) else len(unique)


print(solution([3, 1, 2, 3]))  # 2
print(solution([3, 3, 3, 2, 2, 4]))  # 3
print(solution([3, 3, 3, 2, 2, 2]))  # 2
