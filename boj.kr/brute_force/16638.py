from itertools import combinations


def is_repeat_parentheses(orders):
    for i in range(1, len(orders)):
        if abs(orders[i - 1] - orders[i]) == 2:
            return True

    return False


answer = None
n = int(input())
m = n // 2
expression = list(input())

if n == 1:
    print(expression[0])
    exit()

for i in range(1, (m + 1) // 2 + 1):
    for orders in combinations([j for j in range(1, n, 2)], i):
        if is_repeat_parentheses(orders):
            continue

        _expression = expression[:]

        for order in orders:
            _expression[order - 1] = "(" + _expression[order - 1]
            _expression[order + 1] = _expression[order + 1] + ")"

        calculated = eval("".join(_expression))

        if answer is None or answer < calculated:
            answer = calculated

print(answer)
