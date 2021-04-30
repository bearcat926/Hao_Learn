"""
图中点的层次
给定一个n个点m条边的有向图，图中可能存在重边和自环。

所有边的长度都是1，点的编号为1~n。

请你求出1号点到n号点的最短距离，如果从1号点无法走到n号点，输出-1。

输入格式
第一行包含两个整数n和m。

接下来m行，每行包含两个整数a和b，表示存在一条从a走到b的长度为1的边。

输出格式
输出一个整数，表示1号点到n号点的最短距离。

数据范围
1≤n,m≤10^5
输入样例：
4 5
1 2
2 3
3 4
1 3
1 4
输出样例：
1


所有边的长度都是1 -> 可以使用广度优先搜索

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
P = [-1] * N  # 每一个点到起点的距离
H, E, NE = [-1] * N, [-1] * N, [-1] * N


def insert(a, b):
    global index
    # 头插法
    E[index] = b
    NE[index] = H[a]
    H[a] = index
    index += 1


def bfs():
    Q.push(1)
    P[1] = 0
    while Q.empty() is not True:
        t = Q.pop()
        if t == n:
            print(P[t])
            return

        i = H[t]  # t对应的链表头
        while i != -1:
            j = E[i]  # 与t连通的节点
            if P[j] == -1:  # j没走过
                P[j] = P[t] + 1  # 因为 t -> j, 所以j的步数等于t的步数+1
                Q.push(j)

            i = NE[i]

    print(-1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        insert(a, b)  # 有向图
    bfs()
