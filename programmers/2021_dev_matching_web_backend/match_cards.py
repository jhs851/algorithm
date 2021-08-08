import copy
import sys
from collections import defaultdict
from itertools import permutations
from typing import List


def get_move_count(board: List[List[int]], r: int, c: int, t_r: int, t_c: int) -> int:
    if r == t_r and c == t_c:
        return 0

    n = 4
    result = sys.maxsize
    stack = [(r, c, 0)]
    visited = [(r, c)]
    d_r = [-1, 0, 1, 0]
    d_c = [0, -1, 0, 1]

    while stack:
        _r, _c, count = stack.pop()

        for i in range(4):
            new_r, new_c, new_count = _r + d_r[i], _c + d_c[i], count + 1

            if not 0 <= new_r < n or not 0 <= new_c < n:
                continue

            ctrl_r, ctrl_c = new_r, new_c
            while n > ctrl_r + d_r[i] >= 0 == board[ctrl_r][ctrl_c] and 0 <= ctrl_c + d_c[i] < n:
                ctrl_r += d_r[i]
                ctrl_c += d_c[i]

            if (new_r == t_r and new_c == t_c) or (ctrl_r == t_r and ctrl_c == t_c):
                if result > new_count:
                    result = new_count
                continue

            if (ctrl_r, ctrl_c) not in visited:
                stack.append((ctrl_r, ctrl_c, new_count))
                visited.append((ctrl_r, ctrl_c))

            if (new_r, new_c) not in visited:
                stack.append((new_r, new_c, new_count))
                visited.append((new_r, new_c))

    return result


def solution(board: List[List[int]], r: int, c: int) -> int:
    answer = []
    n = 4
    cards_location = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                cards_location[board[i][j]].append((i, j))

    cards = cards_location.keys()

    for numbers in permutations(cards, len(cards)):
        _board = copy.deepcopy(board)
        _r, _c = r, c
        count = 0

        for number in numbers:
            card_infos = []

            for card_r, card_c in cards_location[number]:
                card_infos.append([card_r, card_c, get_move_count(_board, _r, _c, card_r, card_c)])

            card_infos[0][2] += get_move_count(_board, card_infos[0][0], card_infos[0][1], card_infos[1][0],
                                               card_infos[1][1])
            card_infos[1][2] += get_move_count(_board, card_infos[1][0], card_infos[1][1], card_infos[0][0],
                                               card_infos[0][1])
            sorted_infos = sorted(card_infos, key=lambda item: item[2])
            count += sorted_infos[0][2]
            _r, _c, _ = sorted_infos[1]

            for card_r, card_c, _ in card_infos:
                _board[card_r][card_c] = 0

        answer.append(count)

    return min(answer) + len(cards) * 2


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))  # 14
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 1, 0))  # 16
