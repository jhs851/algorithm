def solution(s):
    replaces = s.replace('{', '').replace('}', '').split(',')
    tuple_dic = {}
    answer = []

    for replace in replaces:
        if replace in tuple_dic:
            tuple_dic[replace] += 1
        else:
            tuple_dic[replace] = 1

    sorted_tuples = sorted(tuple_dic.items(), key=lambda item: item[1], reverse=True)

    for sorted_tuple in sorted_tuples:
        answer.append(int(sorted_tuple[0]))

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111, 20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]
