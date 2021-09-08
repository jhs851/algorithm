from collections import Counter

a = sorted(Counter(input().upper()).items(), key=lambda x: x[1], reverse=True)

if len(a) == 0 or (len(a) > 1 and a[0][1] == a[1][1]):
    print("?")
else:
    print(a[0][0])