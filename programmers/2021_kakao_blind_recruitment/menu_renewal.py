from itertools import combinations


def solution(orders, course):
    answer = []
    all_ways = [{} for _ in range(len(course))]

    for i in range(len(course)):
        for order in orders:
            combination_array = list(map(''.join, combinations(sorted(order), course[i])))

            for combination in combination_array:
                if combination in all_ways[i]:
                    all_ways[i][combination] += 1
                else:
                    all_ways[i][combination] = 1

    for all_way in all_ways:
        max_orders = 0
        sorted_all_way = sorted(all_way.items(), key=lambda item: item[1], reverse=True)

        for s in sorted_all_way:
            if s[1] > 1 and max_orders <= s[1]:
                answer.append(s[0])
                max_orders = s[1]

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))  # ["WX", "XY"]

