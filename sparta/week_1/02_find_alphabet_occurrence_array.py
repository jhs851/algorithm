input = "hello my name is sparta"


# 시간복잡도 O(N)
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for s in string:
        if s.isalpha():
            alphabet_occurrence_array[ord(s) - ord("a")] += 1

    return alphabet_occurrence_array


result = find_max_occurred_alphabet(input)
print(result)