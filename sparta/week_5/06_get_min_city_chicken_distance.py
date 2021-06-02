from itertools import combinations
import sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_house_chicken_distance(house_index, chicken_index_array):
    distance_array = [sys.maxsize] * len(chicken_index_array)
    r, c = house_index

    for chicken_index in chicken_index_array:
        cr, cc = chicken_index
        distance = abs(r - cr) + abs(c - cc)

        if distance == 1:
            return distance
        else:
            distance_array.append(distance)

    return min(distance_array)


def get_min_city_chicken_distance(n, m, city_map):
    house_index_array = []
    chicken_index_array = []
    distance_array = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                house_index_array.append((i, j))
            if city_map[i][j] == 2:
                chicken_index_array.append((i, j))

    for case in combinations(chicken_index_array, m):
        distance = 0

        for house_index in house_index_array:
            distance += get_min_house_chicken_distance(house_index, case)

        distance_array.append(distance)

    return min(distance_array)


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!

city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5, 1, city_map))

city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5, 2, city_map))
