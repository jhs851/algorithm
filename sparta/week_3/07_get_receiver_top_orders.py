top_heights = [6, 9, 5, 7, 4]


# 내꺼
# 시간복잡도 O(N^2^)
# def get_receiver_top_orders(heights):
#     results = [0] * len(heights)
#
#     for i in range(len(heights) - 1, 0, -1):
#         for j in range(i - 1, 0, -1):
#             if heights[i] < heights[j]:
#                 results[i] = j + 1
#                 break
#
#     return results


# 시간복잡도 O(N^2^)
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    while heights:  # O(N)
        height = heights.pop()

        for idx in range(len(heights) - 1, 0, -1):  # O(N)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
