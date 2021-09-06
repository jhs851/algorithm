n = int(input())
m = int(input())
if m > 0:
    b = list(map(int, input().split()))
else:
    b = []
nums = [i for i in range(10) if i not in b]
answer = abs(n - 100)


def possible(x):
    for ch in str(x):
        if int(ch) not in nums:
            return False

    return True


for i in range(1000001):
    if possible(i):
        press = abs(n - i)

        if answer > press + len(str(i)):
            answer = press + len(str(i))

print(answer)

