input = 20


def find_prime_list_under_number(number):
    # 내꺼
    # 시간복잡도 O(N^3^)
    # prime_array = []
    #
    # for i in range(2, number):
    #     is_prime = True
    #
    #     for j in range(2, i):
    #         for k in range(2, i):
    #             if j * k == i:
    #                 is_prime = False
    #
    #     if is_prime:
    #         prime_array.append(i)
    #
    # return prime_array

    # 답안
    # 시간복잡도 O(N)
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)