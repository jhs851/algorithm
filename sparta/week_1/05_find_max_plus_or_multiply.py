input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 내꺼
    # 시간복잡도 O(N)
    max_num = array[0]

    for num in array:
        if max_num > 1 and num > 1:
            max_num *= num
        else:
            max_num += num

    return max_num


result = find_max_plus_or_multiply(input)
print(result)