def solution(priorities, location):
    answer = 0
    importances = sorted(priorities, reverse=True)
    priorities = [(priorities[index], index) for index in range(len(priorities))]

    while True:
        priority, index = priorities.pop(0)

        if priority < importances[0]:
            priorities.append((priority, index))
        else:
            answer += 1

            if index == location:
                return answer

            importances.pop(0)


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
