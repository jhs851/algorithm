# a, b, c -> +3
# d, e, f -> +4
# g, h, i -> +5
# j, k, l -> +6
# m, n, o -> +7
# p, q, r, s -> +8
# t, u, v -> +9
# w, x, y, z -> +10

answer = 0
s = input()

for ch in s:
    if ord('A') <= ord(ch) <= ord('C'):
        answer += 3
    elif ord('D') <= ord(ch) <= ord('F'):
        answer += 4
    elif ord('G') <= ord(ch) <= ord('I'):
        answer += 5
    elif ord('J') <= ord(ch) <= ord('L'):
        answer += 6
    elif ord('M') <= ord(ch) <= ord('O'):
        answer += 7
    elif ord('P') <= ord(ch) <= ord('S'):
        answer += 8
    elif ord('T') <= ord(ch) <= ord('V'):
        answer += 9
    else:
        answer += 10

print(answer)
