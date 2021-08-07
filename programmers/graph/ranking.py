def solution(n, results):
    answer = 0
    chart = [[None] * n for _ in range(n)]

    for winner, loser in results:
        chart[winner - 1][loser - 1] = True
        chart[loser - 1][winner - 1] = False

    for player in range(n):
        losers = [i for i, result in enumerate(chart[player]) if result]

        while losers:
            loser = losers.pop()

            for i, result in enumerate(chart[loser]):
                if result and chart[player][i] is None:
                    chart[player][i] = True
                    chart[i][player] = False
                    losers.append(i)

    for i in range(n):
        if chart[i].count(None) == 1:
            answer += 1

    return answer

# [
#     [None, True, None, None, None],
#     [False, None, False, False, True],
#     [None, True, None, False, None],
#     [None, True, True, None, None],
#     [None, False, None, None, None]
# ]

# [
#     [None, True, None, None, True],
#     [False, None, False, False, True],
#     [None, True, None, False, True],
#     [None, True, True, None, True],
#     [False, False, False, False, None]
# ]