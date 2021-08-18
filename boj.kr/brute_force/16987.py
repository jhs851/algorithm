n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]


def go(index, durabilities):
    # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.
    if index == len(eggs):
        return len([True for durability in durabilities if durability <= 0])

    # 손에 든 계란이 깨졌거나
    if durabilities[index] <= 0:
        return go(index + 1, durabilities)

    # 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
    for i, durability in enumerate(durabilities):
        if index == i:
            continue
        elif durability > 0:
            break
    else:
        return go(index + 1, durabilities)

    answer = 0

    # 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
    for i, (_, weight) in enumerate(eggs):
        if index == i or durabilities[i] <= 0:
            continue

        _durabilities = durabilities[:]
        _durabilities[index] -= weight
        _durabilities[i] -= eggs[index][1]

        temp = go(index + 1, _durabilities)
        if temp > answer:
            answer = temp

    return answer


print(go(0, [durability for durability, weight in eggs]))
