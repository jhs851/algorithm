from collections import defaultdict
from itertools import permutations, combinations


def get_move_count(r1, c1, r2, c2):
    if r1 != r2 and c1 != c2:
        return 2
    elif r1 == r2 and c1 == c2:
        return 0
    else:
        return 1


def solution(board, r, c):
    answer = []
    card_locations = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_locations[board[i][j]].append((i, j))

    cards = card_locations.keys()

    for numbers in permutations(cards, len(cards)):
        move_count = 0
        _r, _c = r, c

        for number in numbers:
            dist_list = sorted([(get_move_count(_r, _c, new_r, new_c), new_r, new_c) for new_r, new_c in card_locations[number]], key=lambda item: item[0])

            for i in range(0, len(dist_list), 2):
                move_count += dist_list[i][0]
                _r, _c = dist_list[i][1], dist_list[i][2]
                new_r, new_c = dist_list[i + 1][1], dist_list[i + 1][2]
                move_count += get_move_count(_r, _c, new_r, new_c)
                _r, _c = new_r, new_c

        answer.append(move_count + len(cards) * 2)

    return min(answer)

print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))  # 14
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))  # 16