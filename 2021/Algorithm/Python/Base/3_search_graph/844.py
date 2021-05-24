"""
走迷宫
给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路，1表示不可通过的墙壁。

最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。

请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。

数据保证(1, 1)处和(n, m)处的数字为0，且一定至少存在一条通路。

输入格式
第一行包含两个整数n和m。

接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。

输出格式
输出一个整数，表示从左上角移动至右下角的最少移动次数。

数据范围
1 ≤ n,m ≤ 100
输入样例：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出样例：
8

BFS - 广度优先搜索



"""

N = 100 + 10


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


G = []  # 地图
D = []  # 每一个点到起点的距离
Q = queue(N * N)


def bfs(n, m):
    Q.push((0, 0))  # 设置起点
    D = [[-1] * m for i in range(n)]  # 初始化D数组
    D[0][0] = 0  # 到起点距离的初值为0

    # 上右下左 -> 0 1 2 3
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while Q.empty() is not True:  # 直到无路可走
        t = Q.pop()  # 拿出一个可以走的点
        for i in range(4):
            # 计算下次可能的点坐标
            y, x = t[0] + dy[i], t[1] + dx[i]
            # 处理可以走且没走过的点
            if 0 <= y < n and 0 <= x < m and G[y][x] == 0 and D[y][x] == -1:
                D[y][x] = D[t[0]][t[1]] + 1
                Q.push((y, x))
    # 因为走过的点不能再走，所以终点存储的值就是到达终点最快的路线所走的步数
    return D[n - 1][m - 1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        temp = list(map(int, input().split()))
        G.append(temp)
    print(bfs(n, m))
