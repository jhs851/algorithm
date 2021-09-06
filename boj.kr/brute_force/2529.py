k = int(input())
a = input().split()
c = [False] * 10
answer = []


def check(x1, x2, o):
    if (o == ">" and x1 < x2) or (o == "<" and x1 > x2):
        return False

    return True


def go(index, number):
    global answer

    if index == k + 1:
        return answer.append(number)

    for i in range(10):
        if c[i] or (index != 0 and not check(int(number[-1]), i, a[index - 1])):
            continue

        c[i] = True
        go(index + 1, number + str(i))
        c[i] = False


go(0, "")
answer.sort()
print(answer[-1])
print(answer[0])
