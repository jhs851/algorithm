e, s, m = map(int, input().split())
_e, _s, _m = 1, 1, 1
answer = 1

while True:
    if _e == e and _s == s and _m == m:
        print(answer)
        break

    _e += 1
    _s += 1
    _m += 1
    answer += 1

    if _e > 15:
        _e = 1
    if _s > 28:
        _s = 1
    if _m > 19:
        _m = 1
