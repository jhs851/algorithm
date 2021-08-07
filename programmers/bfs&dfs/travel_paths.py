from collections import deque


def solution(tickets):
    answer = []
    queue = deque([])

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            queue.append((tickets[i][0], tickets[i][1], tickets[i], tickets[:i] + tickets[i + 1:]))

    while queue:
        start, end, visited, cur_tickets = queue.popleft()

        if end not in [new_start for new_start, _ in cur_tickets]:
            answer.append(visited)
            continue

        for i in range(len(cur_tickets)):
            if end == cur_tickets[i][0]:
                queue.append((cur_tickets[i][0], cur_tickets[i][1], visited + [cur_tickets[i][1]], cur_tickets[:i] + cur_tickets[i + 1:]))

    answer.sort()
    return sorted(answer, key=lambda x: len(x), reverse=True)[0]


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))  # ["ICN", "JFK", "HND", "IAD"]
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
#                 ["ATL", "SFO"]]))  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]]))  # ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"]
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]))  # ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"]

