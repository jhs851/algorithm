input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compressed_lengths = []

    for i in range(1, n // 2 + 1):
        splited = [string[j:i + j] for j in range(0, n, i)]
        count = 1
        compressed = ""

        for j in range(1, len(splited)):
            prev, current = splited[j - 1], splited[j]

            if prev == current:
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += str(count) + splited[-1]
        else:
            compressed += splited[-1]

        compressed_lengths.append(len(compressed))

    return min(compressed_lengths)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("jaaa"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("azaaazdwaaa"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression("bbaabaaadabbbd"))
