# 시간복잡도 O(N)

s = input()
result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])

    if (result == 0 or num == 0):
        result += num
    else:
        result *= num

print(result)

# 답안
# 0 혹은 1인 경우 곱하기보다는 더하기를 수행하는 것이 효율적
result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])

    if (result <= 1 or num <= 1):
        result += num
    else:
        result *= num

print(result)
