from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append(True)
        else:
            if stack:
                stack.pop()

    return len(stack) == 0


def reverse_parentheses(w):
    reverse = ""

    for char in w:
        if char == '(':
            reverse += ')'
        else:
            reverse += '('

    return reverse


def get_correct_parentheses(w):
    if w == "":
        return ""

    u, v = "", ""
    left, right = 0, 0
    queue = deque(w)

    for char in w:
        if char == '(':
            left += 1
        else:
            right += 1

        u += queue.popleft()

        if left == right:
            v = ''.join(list(queue))
            break

    if is_correct_parentheses(u):
        return u + get_correct_parentheses(v)
    else:
        return '(' + get_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
