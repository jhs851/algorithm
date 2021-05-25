import math

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)


def merge(array1, array2):
    array1_index = 0
    array2_index = 0
    result = []

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] > array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index <= len(array1) - 1:
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index <= len(array2) - 1:
        result.append(array2[array2_index])
        array2_index += 1

    return result


def get_max_discounted_price(prices, coupons):
    prices = merge_sort(prices)
    coupons = merge_sort(coupons)
    result = 0

    for i in range(len(prices)):
        if i < len(coupons):
            result += math.floor(prices[i] * (1 - coupons[i] / 100))
        else:
            result += prices[i]

    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
