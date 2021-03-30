"""
Kruskal算法求最小生成树
给定一个 n 个点 m 条边的无向图，图中可能存在重边和自环，边权可能为负数。

求最小生成树的树边权重之和，如果最小生成树不存在则输出 impossible。

给定一张边带权的无向图 G=(V,E)，其中 V 表示图中点的集合，E 表示图中边的集合，n=|V|，m=|E|。

由 V 中的全部 n 个顶点和 E 中 n−1 条边构成的无向连通子图被称为 G 的一棵生成树，其中边的权值之和最小的生成树被称为无向图 G 的最小生成树。

输入格式
第一行包含两个整数 n 和 m。

接下来 m 行，每行包含三个整数 u,v,w，表示点 u 和点 v 之间存在一条权值为 w 的边。

输出格式
共一行，若存在最小生成树，则输出一个整数，表示最小生成树的树边权重之和，如果最小生成树不存在则输出 impossible。

数据范围
1≤n≤10^5,
1≤m≤2∗10^5,
图中涉及边的边权的绝对值均不超过 1000。

输入样例：
4 5
1 2 1
1 3 2
1 4 3
2 3 2
3 4 4
输出样例：
6
========================================
Kruskal算法

    1. 将所有边按权重，从小到大排序
    2. （按序）枚举每条边 a, b, c
        如果a, b不连通
            将这条边加入集合
"""
N = 10 ** 5 + 10
M = N * 2
P = [x for x in range(N)]
EDGE = [(0, 0, 0)] * M


def get_root(x):
    if P[x] != x:
        P[x] = get_root(P[x])
    return P[x]


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b, w = map(int, input().split())
        EDGE[i] = (a, b, w)
    EDGE = sorted(EDGE[:m], key=lambda x: x[2])  # 将所有边按权重排序
    res, cnt = 0, 0  # res表示最小边生成的最小生成树，cnt表示加入集合的点的个数
    for i in range(m):
        t = EDGE[i]
        a, b, w = get_root(t[0]), get_root(t[1]), t[2]
        if a != b:  # merge
            P[a] = b
            res += w
            cnt += 1

    print('impossible' if cnt < n - 1 else res)
