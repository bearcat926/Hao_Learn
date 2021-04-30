"""
spfa求最短路
给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环， 边权可能为负数。

请你求出 1 号点到 n 号点的最短距离，如果无法从 1 号点走到 n 号点，则输出 impossible。

数据保证不存在负权回路。

输入格式
第一行包含整数 n 和 m。

接下来 m 行每行包含三个整数 x,y,z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

输出格式
输出一个整数，表示 1 号点到 n 号点的最短距离。

如果路径不存在，则输出 impossible。

数据范围
1≤n,m≤10^5,
图中涉及边长绝对值均不超过 10000。

输入样例：
3 3
1 2 5
2 3 -3
1 3 4
输出样例：
2
=====================================
SPFA算法

    1. 遍历n次   ->  意义: 从1号点开始, 经过不超过k条边, 存在到达n的最短路径
    2.     遍历所有边(a, b, w)
    3.         D[b] = min(D[b], D[a] + w)
                    ->  优化: 当 D[a] + w < D[b]时, 才会更新D[b]
                            所以只有当D[a]变小, 且D[a]->D[b]时, D[b]才可能变小


    # 可以使用队列进行优化, 将变小的D[a]放入队列, 直到队列为空
    while !queue.empty:
        t = q.pop()
        # t更新的所有出边,
        for i in range(k):
            # 当 D[t] + w < D[b]时
            q.push(b)

    注意：
        1. SPFA算法可以代替堆优化版迪杰斯特拉算法, 解决正数边权的单源最短路问题, 而且更快
        2. 对于网格状图，SPFA算法非常无力

"""
N, M, MAX = 10 ** 5 + 10, 10 ** 5 + 10, 2 ** 32
head, tail = -1, -1
Q, ST = [0] * (N * 2), [False] * N  # Q的长度最好为N, 最差为N*M; ST数组防止存储重复点
H, E, W, NE, D = [-1] * M, [0] * M, [MAX] * M, [-1] * M, [MAX] * N
n, m = 0, 0


def empty():
    return head == tail


def push(x):
    global head
    head += 1
    Q[head] = x


def pop():
    global tail
    tail += 1
    return Q[tail]


def insert(index, a, b, w):
    E[index] = b
    W[index] = w
    NE[index] = H[a]
    H[a] = index


def spfa():
    D[1] = 0
    push(1)
    ST[1] = True
    while empty() is not True:
        t = pop()  # a
        ST[t] = False
        i = H[t]  # a在邻接表中的索引
        while i != -1:
            j = E[i]  # b
            if D[t] + W[i] < D[j]:
                D[j] = D[t] + W[i]
                if ST[j] is not True:
                    push(j)
                    ST[j] = True
            i = NE[i]

    print('impossible' if D[n] > MAX // 2 else D[n])  # MAX // 2 -> 防止负边修改n的值


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b, w = map(int, input().split())
        insert(i, a, b, w)
    spfa()
