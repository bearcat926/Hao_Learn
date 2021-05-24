"""
Dijkstra求最短路 II
给定一个n个点m条边的有向图，图中可能存在重边和自环，所有边权均为非负值。

请你求出1号点到n号点的最短距离，如果无法从1号点走到n号点，则输出-1。

输入格式
第一行包含整数n和m。

接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。

输出格式
输出一个整数，表示1号点到n号点的最短距离。

如果路径不存在，则输出-1。

数据范围
1 ≤ n,m ≤ 1.5×10^5,
图中涉及边长均不小于0，且不超过10000。

输入样例：
3 3
1 2 2
2 3 1
1 3 4
输出样例：
3
=====================================
堆优化版的Dijkstra算法
    1. 初始化距离: D[1] = 0, D[i] = N
    2. 循环并查找不在 S(存放当前已经确定最短距离的点)中的距离最短的点 t, 添加到 S中
                ->  优化：使用堆进行优化, 查找复杂度为O(1), 调整复杂度为O(log_n)  =>  O(n) => O(log_n)
    3. 用 t的边更新其他的点x: D[x] > D[t] + W
    4. 每次循环确定1个点的最小距离, 循环 n次

                ->  一共m条边, 最多调整了m次, 总复杂度为O(m*log_n)

    稀疏图 -> 邻接表

"""
N = int(1.5 * (10 ** 5 + 10))
MAX = 2 ** 32
# HEAP和D都存储最短路值 - PH存储第i个点在堆里面的下标, HP存储堆里面的某个下标对应的点
HEAP, D, PH, HP = [MAX] * N, [MAX] * N, [x for x in range(N)], [x for x in range(N)]
n, size, index = 0, 0, 0
H, E, NE, W = [-1] * N, [-1] * N, [-1] * N, [-1] * N


def heap_swap(a, b):
    # 交换插入值的索引
    PH[HP[a]], PH[HP[b]] = b, a
    # 交换索引对应的节点
    HP[a], HP[b] = HP[b], HP[a]
    # 交换值
    HEAP[a], HEAP[b] = HEAP[b], HEAP[a]


def down(i):
    x = i
    if 2 * i < size and HEAP[2 * i] < HEAP[x]:
        x = 2 * i
    if 2 * i + 1 < size and HEAP[2 * i + 1] < HEAP[x]:
        x = 2 * i + 1
    if x != i:
        heap_swap(x, i)
        down(x)


def up(i):
    while i // 2 >= 1 and HEAP[i // 2] > HEAP[i]:  # 有父亲且父亲大
        heap_swap(i // 2, i)
        i //= 2


def insert(a, b, v):
    global index
    if a != b:  # 解决自环, 但不需要解决重边
        E[index] = b
        W[index] = v
        NE[index] = H[a]
        H[a] = index
        index += 1


def dijkstra():
    global size
    HEAP[1] = D[1] = 0
    while size != 0:
        k = HEAP[1]  # 当前最短路点k
        k_idx = HP[1]  # 最短路点在邻接表中的索引
        # 删除当前最短路点
        heap_swap(1, size)
        size -= 1
        down(1)
        # k在邻接表中的表头
        idx = H[k_idx]
        # 优化检测
        if k_idx == n:
            print(-1 if D[n] == MAX else D[n])
            return
        # 通过k的边, 重新计算最短路
        while idx != -1:
            j = E[idx]  # k -> j
            if D[k_idx] + W[idx] < D[j]:  # 可以修改最小值
                D[j] = min(D[k_idx] + W[idx], D[j])
                HEAP[PH[j]] = D[j]  # 给堆中的j节点赋值
                # 成功计算最短路之后，需要调整堆，使堆顶为最短路点
                down(PH[j])
                up(PH[j])
            idx = NE[idx]

    print(-1 if D[n] == MAX else D[n])


if __name__ == '__main__':
    n, m = map(int, input().split())
    size = n
    for i in range(m):
        x, y, z = map(int, input().split())
        insert(x, y, z)
    dijkstra()