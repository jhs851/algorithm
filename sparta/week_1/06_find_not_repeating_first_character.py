input = "abacabade"


def find_not_repeating_character(string):
    # 내꺼(틀림) 첫 번째로 반복되지 않은 문자열을 반환하지 않음
    # 시간복잡도 O(N)
    # occurrence_array = [0] * 26
    #
    # for character in string:
    #     occurrence_array[ord(character) - ord("a")] += 1
    #
    # for i in range(len(occurrence_array)):
    #     if occurrence_array[i] == 1:
    #         return chr(i + ord("a"))
    #
    # return "_"

    # 답안
    # 시간복잡도 O(N)
    occurrence_array = [0] * 26
    not_repeating_character_array = []

    for character in string:
        occurrence_array[ord(character) - ord("a")] += 1

    for i in range(len(occurrence_array)):
        if occurrence_array[i] == 1:
            not_repeating_character_array.append(chr(i + ord("a")))

    for character in string:
        if character in not_repeating_character_array:
            return character

    return "_"


result = find_not_repeating_character(input)
print(result)