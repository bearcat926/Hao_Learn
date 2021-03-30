"""
Floyd求最短路
给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环，边权可能为负数。

再给定 k 个询问，每个询问包含两个整数 x 和 y，表示查询从点 x 到点 y 的最短距离，如果路径不存在，则输出 impossible。

数据保证图中不存在负权回路。

输入格式
第一行包含三个整数 n,m,k。

接下来 m 行，每行包含三个整数 x,y,z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

接下来 k 行，每行包含两个整数 x,y，表示询问点 x 到点 y 的最短距离。

输出格式
共 k 行，每行输出一个整数，表示询问的结果，若询问两点间不存在路径，则输出 impossible。

数据范围
1≤n≤200,
1≤k≤n2
1≤m≤20000,
图中涉及边长绝对值均不超过 10000。

输入样例：
3 3 2
1 2 1
2 3 2
1 3 1
2 1
1 3
输出样例：
impossible
1
=====================================
Floyd算法

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    基于DP, <hao_mark>
"""
N, M, MAX = 200 + 10, 20000 + 10, 2 ** 32
D = [[MAX] * N for i in range(N)]


def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    # 处理自环(由于不存在负环回路，则自环必定为正)
    for i in range(1, n + 1):
        D[i][i] = 0
    for i in range(m):
        x, y, z = map(int, input().split())
        D[x][y] = min(D[x][y], z)  # 处理重边, 只保留一条最小边
    floyd()
    for i in range(k):
        x, y = map(int, input().split())
        print('impossible' if D[x][y] > (MAX // 2) else D[x][y])
