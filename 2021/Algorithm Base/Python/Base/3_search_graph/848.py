"""
有向图的拓扑序列
给定一个n个点m条边的有向图，点的编号是1到n，图中可能存在重边和自环。

请输出任意一个该有向图的拓扑序列，如果拓扑序列不存在，则输出-1。

若一个由图中所有点构成的序列A满足：对于图中的每条边(x, y)，x在A中都出现在y之前，则称A是该图的一个拓扑序列。

输入格式
第一行包含两个整数n和m

接下来m行，每行包含两个整数x和y，表示存在一条从点x到点y的有向边(x, y)。

输出格式
共一行，如果存在拓扑序列，则输出任意一个合法的拓扑序列即可。

否则输出-1。

数据范围
1≤n,m≤10^5
输入样例：
3 3
1 2
2 3
1 3
输出样例：
1 2 3

有向图的拓扑序列

    拓扑图 -> 有向无环图

        入度: 指向节点的边数

        出度: 节点外指的边数

        所有入度为0的点都可以作为起点

        一个有向无环图，一定存在一个入度为0的点
"""


class queue:
    def __init__(self, size):
        self.D = [0] * size
        self.head = -1
        self.tail = -1

    def empty(self):
        return self.head == self.tail

    def push(self, e):
        if self.tail < len(self.D):
            self.tail += 1
            self.D[self.tail] = e

    def pop(self):
        if not self.empty():
            self.head += 1
            return self.D[self.head]

    def query(self):
        if not self.empty():
            return self.D[self.head + 1]


N = 10 ** 5 + 10
index, n = 0, 0
Q = queue(N * 2)
IM = [0] * N
H, E, NE = [-1] * N, [-1] * N, [-1] * N  # 无向图有两条边，所以开2N数组


def insert(a, b):
    global index
    # 头插法
    E[index] = b
    NE[index] = H[a]
    H[a] = index
    index += 1


def top_sort():
    # 找到第一个入度为0的点
    for i in range(n):
        if IM[i] == 0:
            Q.push(IM[i])

    while Q.empty() is not True:
        t = Q.pop()

        i = H[t]  # t对应的链表头
        while i != -1:
            j = E[i]  # t指向的节点
            IM[j] -= 1
            if IM[j] == 0:
                Q.push(j)

    return Q.tail == n - 1


"""
因为环上的点入度都不为0, 因此不能进入队列中
因此当对头等于n - 1时, 队列中一共进入了n个点, 则该图为有向无环图
且此时, 若x在y之前入队, 则x必定在y之前 -> 队列中的数组就是一个拓扑序列（不唯一）
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        insert(a, b)
        IM[b] += 1  # b的入度 + 1
    if top_sort():
        for i in range(n):
            print(Q.D[i], end=' ')
    else:
        print(-1)
