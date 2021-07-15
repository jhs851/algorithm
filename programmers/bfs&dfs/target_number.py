def solution(numbers, target):
    answer = 0
    stack = [(numbers[0], 0), (-numbers[0], 0)]

    while stack:
        value, index = stack.pop()
        new_index = index + 1

        plus = value + numbers[new_index]
        minus = value - numbers[new_index]

        if new_index == len(numbers) - 1:
            if plus == target:
                answer += 1
            elif minus == target:
                answer += 1

            continue

        stack.append((plus, new_index))
        stack.append((minus, new_index))

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
