"""
染色法判定二分图
给定一个 n 个点 m 条边的无向图，图中可能存在重边和自环。

请你判断这个图是否是二分图。

输入格式
第一行包含两个整数 n 和 m。

接下来 m 行，每行包含两个整数 u 和 v，表示点 u 和点 v 之间存在一条边。

输出格式
如果给定图是二分图，则输出 Yes，否则输出 No。

数据范围
1≤n,m≤105
输入样例：
4 4
1 3
1 4
2 3
2 4
输出样例：
Yes
========================================
二分图

    染色法 O(n + m)

    匈牙利算法 最坏 O(m*n) , 一般情况远小于该值
========================================
1. 当且仅当，图中不含有奇数环时，是二分图
2. 由于图中不含奇数环，因此染色过程中一定没有矛盾
========================================
Python解法，有两个要注意的点
1. 由于DFS会报错，所以改成BFS.
2. BFS从1开始只会遍历所在的连通分量，所以要循环所有color[i] = -1的点
========================================
# dfs 代码，由于递归层数过多而报错
N = 10 ** 5 + 10
M = 2 * N
index = 0
H, E, NE = [-1] * N, [-1] * M, [-1] * M  # 无向图有两条边，所以开2N数组
color = [-1] * N


def add(a, b):
    global index
    E[index] = b
    NE[index] = H[a]
    H[a] = index
    index += 1


def dfs(x, c):
    color[x] = c
    j = H[x]
    while j != -1:
        t = E[j]
        t_c = color[t]
        if t_c == c:  # 染了其他颜色
            return False
        elif t_c == -1:
            if not dfs(t, 1 - c):
                if n > 1000:
                    print(t, 1 - c)
                return False
        j = NE[j]
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        add(a, b)
        add(b, a)
    flag = True
    for i in range(1, n + 1):
        if color[i] == -1:
            if not dfs(1, 0):
                flag = False
                break
    print('Yes' if flag else 'No')
"""
N = 10 ** 5 + 10
M = 2 * N
head, tail, index = -1, -1, 0
color = [-1] * N
Q, H, E, NE = [-1] * N, [-1] * N, [-1] * M, [-1] * M  # 无向图有两条边，所以开2N数组


def add(a, b):
    global index
    E[index] = b
    NE[index] = H[a]
    H[a] = index
    index += 1


def bfs():
    global head, tail
    for i in range(1, n + 1):  # 循环所有点，以便遍历所有连通块
        if color[i] == -1:
            color[i] = 0  # 第一层的节点都为0，之后则为1,0,1,0...
            # bfs 代码
            head += 1  # push
            Q[head] = i
            while head != tail:
                tail += 1  # pop
                t = Q[tail]
                t_c = color[t]
                i = H[t]
                while i != -1:
                    j = E[i]
                    c = color[j]
                    if t_c == c:  # 染了其他颜色
                        return False
                    elif c == -1:  # 没染颜色
                        color[j] = 1 - t_c
                        head += 1  # push
                        Q[head] = j
                    i = NE[i]
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        add(a, b)
        add(b, a)

    print('Yes' if bfs() else 'No')