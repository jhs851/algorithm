import sys

sys.setrecursionlimit(10 ** 6)  # 이걸 안해주면 횟수제한에 걸려서 재귀가 막혀버림

preorder = []
postorder = []


def solution(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)  # 어떤 레벨이 있는지 파악
    nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)),
                   key=lambda x: (-x[1][1], x[1][0]))  # 노드좌표와 인덱스를 서로 연결 해 줌
    order(nodes, levels, 0)

    return [preorder, postorder]


def order(nodes, levels, cur_level):
    _nodes = nodes[:]
    cur_node = _nodes.pop(0)
    preorder.append(cur_node[0])
    if _nodes:
        for i in range(len(_nodes)):
            if _nodes[i][1][1] == levels[cur_level + 1]:
                if _nodes[i][1][0] < cur_node[1][0]:
                    order([node for node in nodes if node[1][0] < cur_node[1][0]], levels, cur_level + 1)
                else:
                    order([node for node in nodes if node[1][0] > cur_node[1][0]], levels, cur_level + 1)
    postorder.append(cur_node[0])


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2],
                [2, 2]]))  # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
