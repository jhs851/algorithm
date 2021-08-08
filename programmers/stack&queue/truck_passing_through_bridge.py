def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = [[weight, 0] for weight in truck_weights]
    passing = []

    while truck_weights or passing:
        sum_weights = 0

        for p in passing:
            sum_weights += p[0]

        if truck_weights and sum_weights + truck_weights[0][0] <= weight:
            passing.append(truck_weights.pop(0))

        for i in range(len(passing)):
            w, s = passing[i]
            passing[i] = [w, s + 1]

        if passing[0][1] >= bridge_length:
            passing.pop(0)

        answer += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
