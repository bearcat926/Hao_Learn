"""
多重背包问题 I
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0 < N,V ≤ 100
0 < vi,wi,si ≤ 100
输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
"""
N = 100 + 10
V, W, S = [0] * N, [0] * N, [0] * N
F = [[0] * N for i in range(N)]

if __name__ == '__main__':
    n, v = map(int, input().split())
    for i in range(n):
        V[i + 1], W[i + 1], S[i + 1] = map(int, input().split())
    # dp
    for i in range(1, n + 1):
        for j in range(0, v + 1):
            k = 0
            while k <= S[i] and k * V[i] <= j:
                F[i][j] = max(F[i][j], F[i - 1][j - k * V[i]] + k * W[i])
                k += 1
    print(F[n][v])
