"""
spfa判断负环
给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环， 边权可能为负数。

请你判断图中是否存在负权回路。

输入格式
第一行包含整数 n 和 m。

接下来 m 行每行包含三个整数 x,y,z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

输出格式
如果图中存在负权回路，则输出 Yes，否则输出 No。

数据范围
1≤n≤2000,
1≤m≤10000,
图中涉及边长绝对值均不超过 10000。

输入样例：
3 3
1 2 -1
2 3 4
3 1 -4
输出样例：
Yes
=====================================
SPFA算法判断负权回环存在

若CNT[n] >= n
则 1 -> n的路径上, 至少存在n条边, 即存在n + 1个点

由此得出1 -> n的路径上, 至少存在一个点k出现了两次, 即一个点被走过两次, 即存在回环
且因 SPFA算法的特性, 若点k的值不曾减小, 则该点不会出现两次, 因此点k附近必定存在负权值

证毕: 1 -> n的路径上, 存在负权回环

"""
N, M, MAX = 2000 + 10, 10000 + 10, 2 ** 32
D, CNT = [MAX] * N, [0] * N  # CNT表示当前最短路的边数
head, tail = -1, -1
Q, ST = [0] * (M * N), [False] * (M * N)  # Q的长度最好为N, 最差为N*M; ST数组防止存储重复点
H, E, W, NE = [-1] * M, [0] * M, [MAX] * M, [-1] * M
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
    global n
    D[1] = 0
    for i in range(1, n + 1):  # 题目为判断图中是否存在负权回路, 因此需要对所有的进行检查
        push(i)
        ST[i] = True
    while empty() is not True:
        t = pop()
        ST[t] = False
        i = H[t]
        while i != -1:
            j = E[i]
            if D[j] > D[t] + W[i]:
                D[j] = D[t] + W[i]
                CNT[j] = CNT[t] + 1  # 计算当前最短路的边数
                if CNT[j] >= n:  # 负权回环一般会使程序死循环, 需要设置出口
                    print('Yes')
                    return
                if D[j] is not True:
                    push(j)
                    ST[j] = True
            i = NE[i]
    print('No')


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        a, b, w = map(int, input().split())
        insert(i, a, b, w)
    spfa()