def solution(n, k, cmd):
    answer = ["O"] * n
    up = [-1] + [i for i in range(n - 1)]
    down = [i for i in range(1, n)] + [-1]
    removed = []

    for command in cmd:
        command = command.split()

        if command[0] == "D":
            for _ in range(int(command[1])):
                k = down[k]
        elif command[0] == "U":
            for _ in range(int(command[1])):
                k = up[k]
        elif command[0] == "C":
            if up[k] != -1:
                down[up[k]] = down[k]

            if down[k] != -1:
                up[down[k]] = up[k]

            answer[k] = "X"
            removed.append(k)
            k = down[k] if down[k] != -1 else up[k]
        else:
            recover_index = removed.pop()

            if up[recover_index] != -1:
                down[up[recover_index]] = recover_index

            if down[recover_index] != -1:
                up[down[recover_index]] = recover_index

            answer[recover_index] = "O"

    return "".join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]) == "OOOOXOOO")
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]) == "OOXOXOOO")
