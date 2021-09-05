t = int(input())

for _ in range(t):
    k, n = map(int, [input(), input()])
    apartment = [[i + 1 for i in range(n)]]

    for i in range(k):
        apartment.append([sum(apartment[i][:j + 1]) for j in range(n)])

    print(apartment[k][n - 1])

# k층에 n호에는 몇 명이 살고 있는지 출력
# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다

# 1 3  6
# 2 3  10

# 3층 = 1(1) 2(5) 3(15) 4(35) 5(70)
# 2층 = 1(1) 2(4) 3(10) 4(20) 5(35)
# 1층 = 1(1) 2(3) 3(6)  4(10) 5(15)
# 0층 = 1(1) 2(2) 3(3)  4(4)  5(5)

