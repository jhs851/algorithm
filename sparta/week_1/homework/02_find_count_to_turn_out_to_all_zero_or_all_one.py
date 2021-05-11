input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 내꺼
    # 시간복잡도 O(N)
    # counts = [0, 0]
    #
    # for i in range(2):
    #     repeating = False
    #     count = 0
    #
    #     for num in string:
    #         if num == str(i) and repeating == False:
    #             repeating = True
    #             count += 1
    #         elif num != str(i) and repeating == True:
    #             repeating = False
    #
    #     counts[i] = count
    #
    # return min(counts)

    # 답안
    # 시간복잡도 O(N)
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            elif string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 모두 0으로 바꾼 횟수와
# 모두 1로 바꾼 횟수 중 가장 낮은 횟수
# 0으로 바꿀 때의 횟수는 1의 묶음들별로 문자열을 나누면 0으로 바꿀 횟수
