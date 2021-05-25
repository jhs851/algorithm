s = "(())()"


def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if len(stack) == 0 and char == ')':
            return False
        elif char == '(':
            stack.append(True)
        else:
            stack.pop()

    return len(stack) == 0


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
