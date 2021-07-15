def solution(s):
    answer = []

    for i in range(1, len(s) // 2 + 1):
        splited = [s[j:j + i] for j in range(0, len(s), i)]
        count = 1
        compressed = ""

        for j in range(1, len(splited)):
            if splited[j - 1] == splited[j]:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + splited[j - 1]
                else:
                    compressed += splited[j - 1]

                count = 1

        if count > 1:
            compressed += str(count) + splited[-1]
        else:
            compressed += splited[-1]

        answer.append(len(compressed))

    return min(answer)


print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
