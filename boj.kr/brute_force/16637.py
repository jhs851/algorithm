from itertools import combinations

n = int(input())
expression = list(input())
answer = set()


def is_repeat_parentheses(orders):
    for i in range(1, len(orders)):
        if orders[i] - orders[i - 1] == 2:
            return True

    return False


def calculate(e):
    result = e[0]

    for i in range(1, len(e), 2):
        result = str(eval(result + "".join(e[i:i + 2])))

    return int(result)


for i in range(1, (n // 2 + 1) // 2 + 1):
    for orders in combinations([j for j in range(1, n, 2)], i):
        if is_repeat_parentheses(orders):
            continue

        _expression = expression[:]

        for order in orders:
            _expression = _expression[:order - 1] + [str(eval("".join(_expression[order - 1:order + 2])))] + ["+", "0"] + _expression[order + 2:]

        answer.add(calculate(_expression))

print(max(answer))

# 괄호의 최대 수는 정수의 수 // 2
# 괄호는 연속된 연산자끼리 붙을 수 없다

# 9
# 3+8*7-9*2
# 136

# 5
# 8*3+5
# 64

# 7
# 8*3+5+2
# 66

# 19
# 1*2+3*4*5-6*7*8*9*0
# 0

# 19
# 1*2+3*4*5-6*7*8*9*9
# 426384

# 19
# 1-9-1-9-1-9-1-9-1-9
# 24
