input = "abcba"


def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False

    return True


print(is_palindrome(input))
