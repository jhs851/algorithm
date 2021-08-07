type = input()
answer = 1

for i in range(len(type)):
    if type[i] == "d":
        answer *= 9 if i > 0 and type[i - 1] == type[i] else 10
    else:
        answer *= 25 if i > 0 and type[i - 1] == type[i] else 26

print(answer)

