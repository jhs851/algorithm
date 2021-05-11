input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 내꺼
    # 시간복잡도 O(N)
    # alphabet_occurrence_array = [0] * 26
    #
    # for s in string:
    #     if s.isalpha():
    #         alphabet_occurrence_array[ord(s) - ord("a")] += 1
    #
    # max_index = 0
    #
    # for index in range(1, len(alphabet_occurrence_array)):
    #     if alphabet_occurrence_array[max_index] < alphabet_occurrence_array[index]:
    #         max_index = index
    #
    # return chr(max_index + 97)

    # 답안
    # 시간복잡도 O(N)
    alphabet_occurrence_array = [0] * 26

    for s in string:
        if s.isalpha():
            alphabet_occurrence_array[ord(s) - ord("a")] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[0]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)