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
    # 시간복잡도 O(N^2^)
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0

        for char in string:
            if alphabet == char:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)