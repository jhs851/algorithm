n = int(input())

count = 1
cur_node = 1

while n > cur_node:
    cur_node += count * 6
    count += 1

print(count)