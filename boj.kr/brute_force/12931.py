n = int(input())
a = [format(x, "b") for x in list(map(int, input().split()))]

print(max([len(x) - 1 for x in a]) + sum([x.count("1") for x in a]))
