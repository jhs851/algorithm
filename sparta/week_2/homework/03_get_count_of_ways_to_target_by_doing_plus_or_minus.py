numbers = [2, 3, 1]
target_number = 0
result = []
result_count = 0

# 1. +2 +3 +1 = 6       +++
# 2. +2 +3 -1 = 4       ++-
# 3. +2 -3 +1 = 0 타겟!  +-+
# 4. +2 -3 -1 = -2      +--
# 5. -2 +3 +1 = 2
# 6. -2 +3 -1 = 0 타겟!
# 7. -2 -3 +1 = -4
# 8. -2 -3 -1 = -7

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N - 1의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를
# 추가하면 됨


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array):
        if current_sum == target_number:
            global result_count
            result_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], all_ways)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], all_ways)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0, 0, result)  # 5를 반환해야 합니다!
print(result_count)
