array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


# 내꺼
# 시간복잡도 O(N)
# def merge(array1, array2):
#     result = []
#     index_a = 0
#     index_b = 0
#
#     while len(result) != len(array1) + len(array2):
#         if index_a == len(array1):
#             result.append(array2[index_b])
#             index_b += 1
#             continue
#         elif index_b == len(array2):
#             result.append(array1[index_a])
#             index_a += 1
#             continue
#
#         if array1[index_a] < array2[index_b]:
#             result.append(array1[index_a])
#             index_a += 1
#         elif array1[index_a] > array_b[index_b]:
#             result.append(array2[index_b])
#             index_b += 1
#
#     return result

def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
            array1_index += 1

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
