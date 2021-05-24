def stack_sequence(n, sequence):
    stack = []
    guess = 0
    result = []

    for i in range(n):
        stack.append(i + 1)
        result.append('+')

        while stack and guess <= len(sequence) - 1 and stack[-1] == sequence[guess]:
            stack.pop()
            result.append('-')
            guess += 1

    if stack:
        return print("No")

    for value in result:
        print(value)


sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)
