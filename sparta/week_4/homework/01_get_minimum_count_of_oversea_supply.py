import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    supplies_dict = {}
    count = 0

    for i in range(len(dates)):
        supplies_dict[dates[i]] = supplies[i]

    while stock < k:
        heap = []

        for date in supplies_dict:
            if date <= stock:
                heapq.heappush(heap, date * -1)

        max_supply_date = heapq.heappop(heap) * -1
        stock += supplies_dict[max_supply_date]
        del supplies_dict[max_supply_date]
        count += 1

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))
