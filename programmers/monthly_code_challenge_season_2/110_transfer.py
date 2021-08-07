from collections import deque


def solution(s):
    answer = []

    for string in s:
        if "110" not in string:
            answer.append(string)
            continue

        stack = []
        one_one_zero_count = 0

        # 110 제거
        for char in string:
            stack.append(char)

            if stack[-3:] == list("110"):
                one_one_zero_count += 1

                for i in range(3):
                    stack.pop()

        # 110 붙이기
        queue = deque()

        while stack:
            if stack[-1] == "1":
                queue.append(stack.pop())
            else:
                break

        for _ in range(one_one_zero_count):
            queue.appendleft("0")
            queue.appendleft("1")
            queue.appendleft("1")

        while stack:
            queue.appendleft(stack.pop())

        answer.append("".join(queue))

    return answer


print(solution(["1110", "100111100", "0111111010"]))  # ["1101","100110110","0110110111"]
