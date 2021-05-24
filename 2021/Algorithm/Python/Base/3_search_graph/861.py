"""
二分图的最大匹配
给定一个二分图，其中左半部包含 n1 个点（编号 1∼n1），右半部包含 n2 个点（编号 1∼n2），二分图共包含 m 条边。

数据保证任意一条边的两个端点都不可能在同一部分中。

请你求出二分图的最大匹配数。

二分图的匹配：给定一个二分图 G，在 G 的一个子图 M 中，M 的边集 {E} 中的任意两条边都不依附于同一个顶点，则称 M 是一个匹配。

二分图的最大匹配：所有匹配中包含边数最多的一组匹配被称为二分图的最大匹配，其边数即为最大匹配数。

输入格式
第一行包含三个整数 n1、 n2 和 m。

接下来 m 行，每行包含两个整数 u 和 v，表示左半部点集中的点 u 和右半部点集中的点 v 之间存在一条边。

输出格式
输出一个整数，表示二分图的最大匹配数。

数据范围
1 ≤ n1,n2 ≤ 500,
1 ≤ u ≤ n1,
1 ≤ v ≤ n2,
1 ≤ m ≤ 10^5
输入样例：
2 2 4
1 1
1 2
2 1
2 2
输出样例：
2
===================================
匈牙利算法 - 世称月老算法

"""
N, M = 500 + 10, 10 ** 5 + 10
H, E, NE = [-1] * N, [-1] * M, [-1] * M
index, n, m = 0, 0, 0
MATCH = [0] * N  # 存储妹子与其男票的映射
ST = []  # 预定数组


def insert(a, b):
    global index
    E[index] = b
    NE[index] = H[a]
    H[a] = index
    index += 1


def match(x):
    i = H[x]
    while i != -1:
        y = E[i]
        if not ST[y]:  # 这轮妹子没被预定
            ST[y] = True
            if MATCH[y] == 0 or match(MATCH[y]):  # 没有男票或者原来的男票可以找到其他妹子
                MATCH[y] = x
                return True
        i = NE[i]
    return False


if __name__ == '__main__':
    n1, n2, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
        insert(a, b)

    res = 0
    for x in range(1, n1 + 1):  # 循环左边
        ST = [False] * N  # 因为每次匹配的预定情况都是不一样的所以每轮匹配都要初始化预定数组
        if match(x):
            res += 1

    print(res)