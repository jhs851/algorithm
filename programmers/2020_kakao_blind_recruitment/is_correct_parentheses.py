from collections import deque


def is_correct_parentheses(w):
    stack = []

    for char in w:
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


def solution(p):
    if p == "":
        return ""

    queue = deque(p)
    u, v = "", ""
    left, right = 0, 0

    for char in p:
        if char == '(':
            left += 1
        else:
            right += 1

        u += queue.popleft()

        if left == right:
            v = ''.join(queue)
            break

    if is_correct_parentheses(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse_parentheses(u[1: -1])


print(solution("(()())()"))

