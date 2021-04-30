"""
分组背包问题
有 N 组物品和一个容量是 V 的背包。

每组物品有若干个，同一组内的物品最多只能选一个。
每件物品的体积是 v_ij，价值是 w_ij，其中 i 是组号，j 是组内编号。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。

输出最大价值。

输入格式
第一行有两个整数 N，V，用空格隔开，分别表示物品组数和背包容量。

接下来有 N 组数据：

每组数据第一行有一个整数 Si，表示第 i 个物品组的物品数量；
每组数据接下来有 Si 行，每行有两个整数 v_ij,w_ij，用空格隔开，分别表示第 i 个物品组的第 j 个物品的体积和价值；
输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<Si≤100
0<v_ij,w_ij≤100
输入样例
3 5
2
1 2
2 4
1
3 4
1
4 5
输出样例：
8
"""

N = 100 + 10
V, W = [[0] * N for i in range(N)], [[0] * N for i in range(N)]
F = [0] * N

if __name__ == '__main__':
    n, v = map(int, input().split())
    for i in range(1, n + 1):
        g = int(input())
        for j in range(1, g + 1):
            V[i][j], W[i][j] = map(int, input().split())
    # dp
    for i in range(1, n + 1):
        for j in range(v, -1, -1):  # 逆序
            for k in range(1, len(V[i])):  # 存储的下标从1开始
                if j >= V[i][k]:
                    F[j] = max(F[j], F[j - V[i][k]] + W[i][k])
    print(F[v])