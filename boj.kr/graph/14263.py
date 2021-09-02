# 실제 카드의 크기와
# 현재 카드가 노출되는 수를 비교해서 손상된 카드인지 확인
# 손상되지 않았다면 루트 노드
# 루트노드부터 손상시킨 카드가 선행 노드
# 그래프로 정리하고 위상 정렬 및 같은 레벨의 노드는 사전 오름차순 정렬
# 1. 실제 카드의 크기와 현재 카드가 노출되는 수 저장
# (1) NM만큼 돌면서 카드를 찾고 -> NM
#   (2) 해당 카드의 실제 크기와 노출되는 수를 비교 -> NM
#    NM^2 -> 62,500
# 2. 그래프로 정리
import sys

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
sizes = []
exposures = []


def get_size(x, y, target):
    return


def get_exposure(x, y, target):
    return


for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            sizes.append(get_size(i, j, grid[i][j]))
            exposures.append(get_exposure(i, j, grid[i][j]))
