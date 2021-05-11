s = input()
result = []
sum = 0
hasInt = False

for v in s:
    if v.isalpha():
        result.append(v)
    else:
        hasInt = True
        sum += int(v)

result.sort()

if hasInt:
    result.append(str(sum))

print("".join(result))
