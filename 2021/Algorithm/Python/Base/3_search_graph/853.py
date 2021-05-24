"""
有边数限制的最短路
给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环， 边权可能为负数。

请你求出从 1 号点到 n 号点的最多经过 k 条边的最短距离，如果无法从 1 号点走到 n 号点，输出 impossible。

注意：图中可能 存在负权回路 。

输入格式
第一行包含三个整数 n,m,k。

接下来 m 行，每行包含三个整数 x,y,z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

输出格式
输出一个整数，表示从 1 号点到 n 号点的最多经过 k 条边的最短距离。

如果不存在满足条件的路径，则输出 impossible。

数据范围
1 ≤ n,k ≤ 500,
1 ≤ m ≤ 10000,
任意边长的绝对值不超过 10000。

输入样例：
3 3 1
1 2 1
2 3 1
1 3 3
输出样例：
3
=====================================
Bellman-ford算法

    1. 遍历n次   ->  意义: 从1号点开始, 经过不超过k条边, 存在到达n的最短路径
    2.     遍历所有边(a, b, w)
    3.         D[b] = min(D[b], D[a] + w)

    计算之后，对于所有的边都满足三角不等式(D[b] <= D[a] + w), 该过程被称为松弛操作

    当图中存在负权回路, 一般情况下图中不存在最短路
              3          5           2
         1 -------> 2 -------> 3 -------> 5
                     \       /
                      \     /
                    -4 \   / -2
                        \ /
                         4

        如图, 每沿 2 -> 3 -> 4 -> 2 走一次, 最短路就-1, 因此该图不存在最短路

"""
N, M, MAX = 500 + 10, 10000 + 10, 2 ** 32
A, B, W, D, BACK = [0] * M, [0] * M, [0] * M, [MAX] * N, []
n, m, k = 0, 0, 0


def insert(index, a, b, w):
    A[index] = a
    B[index] = b
    W[index] = w


def bellman_ford():
    D[1] = 0
    for i in range(k):
        BACK = [x for x in D]
        for j in range(m):
            D[B[j]] = min(BACK[A[j]] + W[j], D[B[j]])  # BACK数组防止边的增量传递
    print('impossible' if D[n] > MAX // 2 else D[n])  # MAX // 2 -> 防止负边修改n的值


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    for i in range(m):
        a, b, w = map(int, input().split())
        insert(i, a, b, w)
    bellman_ford()
