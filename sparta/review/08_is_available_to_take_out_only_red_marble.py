# 문제링크 https://www.notion.so/5-f51f57c84aef4626b580a5937adabca9#b9d162f860734c48aad924aed7ec71fb

from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]


def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    return


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))
