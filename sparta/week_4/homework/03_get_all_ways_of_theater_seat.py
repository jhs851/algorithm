seat_count = 9
vip_seat_array = [4, 7]


# 1. 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다.
# 2. 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 3. 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
# 4. VIP 회원은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.

# 123456789
# 123456798

# 123465789
# 123465798

# 132456789
# 132456798
# 132465789
# 132465798

# 213456789
# 213456798
# 213465789
# 213465798

# 만약 1234 4개라면
# 1234
# 1243
# 1324
# 2134
# 2143

# 만약 12345 5개라면
# 12345
# 12354
# 12435
# 13245
# 13254
# 21345
# 21354
# 21435

# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5 - 8

def get_all_ways_count(n, memo):
    if n in memo:
        return memo[n]

    memo[n] = get_all_ways_count(n - 1, memo) + get_all_ways_count(n - 2, memo)
    return memo[n]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    memo = {
        1: 1,
        2: 2,
        3: 3,
    }
    result = 1
    n = 0

    for i in range(total_count):
        if i + 1 in fixed_seat_array:
            result *= get_all_ways_count(n, memo)
            n = 0
            continue

        n += 1

    result *= get_all_ways_count(total_count - fixed_seat_array[-1], memo)

    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))
