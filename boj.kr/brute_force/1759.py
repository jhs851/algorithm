# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다
l, c = map(int, input().split())
a = sorted(input().split())
answer = [0] * l
vowels = ('a', 'e', 'i', 'o', 'u')


def possible(password):
    vowel_count = 0
    consonant_count = 0

    for p in password:
        if p in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count >= 1 and consonant_count >= 2


def go(index, selected):
    if selected == l:
        if possible(answer):
            print("".join(answer))
        return

    if index >= c:
        return

    answer[selected] = a[index]
    go(index + 1, selected + 1)
    answer[selected] = 0
    go(index + 1, selected)


go(0, 0)

