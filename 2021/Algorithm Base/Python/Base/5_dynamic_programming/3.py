"""
完全背包问题
有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。

第 i 种物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
10
=======================================
解决方案：

    1. 去掉 k个物品i的体积后求Max，f(i-1, j-k*V[i])
    2. 再加 k个物品i

    状态转移方程为：f(i, j) = f(i-1, j-k*V[i]) + k*W[i]
"""
"""
# 朴素 (TLE)
N = 1000 + 10
V, W = [0] * N, [0] * N
F = [[0] * N for i in range(N)]

if __name__ == '__main__':
    n, v = map(int, input().split())
    for i in range(n):
        V[i + 1], W[i + 1] = map(int, input().split())
    # dp
    for i in range(1, n + 1):  # [1, n]
        for j in range(v + 1):  # [0, v]
            k = 0
            while k * V[i] <= j:  # [0, j // V[i]]
                F[i][j] = max(F[i][j], F[i - 1][j - k * V[i]] + k * W[i])
                k += 1
    print(F[n][v])
"""

"""
优化为二维

    f(i, j)   = MAX(F[i-1][j]  , (F[i-1][j-V[i]]+w), (F[i-1][j-2*V[i]]+2*w), ..., F[i-1][j-k*V[i]]+k    *W[i])
    f(i, j-v) = MAX(              F[i-1][j-v]      , (F[i-1][j-  V[i]]+  w), ..., F[i-1][j-k*V[i]]+(k-1)*W[i])
    
    优化后的状态转移方程为：1. F[i][j] = max(F[i][j], F[i - 1][j])
                        2. F[i][j] = max(F[i][j], F[i][j - V[i]] + W[i]) (j >= V[i])
"""

N = 1000 + 10
V, W = [0] * N, [0] * N
F = [[0] * N for i in range(N)]

if __name__ == '__main__':
    n, v = map(int, input().split())
    for i in range(n):
        V[i + 1], W[i + 1] = map(int, input().split())
    # dp
    for i in range(1, n + 1):  # [1, n]
        for j in range(v + 1):  # [0, v]
            F[i][j] = F[i - 1][j]
            if j >= V[i]:
                F[i][j] = max(F[i][j], F[i][j - V[i]] + W[i])
    print(F[n][v])

"""
优化为一维

    01背包:
        F[i][j] = max(F[i][j], F[i - 1][j - V[i]] + W[i])
    完全背包:
        F[i][j] = max(F[i][j], F[i][j - V[i]] + W[i])
        
    因此完全背包不存在优先计算 i - 1的问题，无需逆序计算状态
"""

N = 1000 + 10
V, W = [0] * N, [0] * N
F = [0] * N

if __name__ == '__main__':
    n, v = map(int, input().split())
    for i in range(n):
        V[i + 1], W[i + 1] = map(int, input().split())
    # dp
    for i in range(1, n + 1):  # [1, n]
        for j in range(V[i], v + 1):  # [V[i], v]
            F[j] = max(F[j], F[j - V[i]] + W[i])
    print(F[v])
