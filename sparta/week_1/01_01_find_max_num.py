input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 내꺼
    # 시간복잡도 O(N)
    # max_num = 0
    #
    # for value in array:
    #     if max_num < value:
    #         max_num = value
    #
    # return max_num

    # 답안
    # 시간복잡도 O(N^2^)
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)