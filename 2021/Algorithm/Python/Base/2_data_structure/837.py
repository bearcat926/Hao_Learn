"""
连通块中点的数量
给定一个包含n个点（编号为1~n）的无向图，初始时图中没有边。

现在要进行m个操作，操作共有三种：

“C a b”，在点a和点b之间连一条边，a和b可能相等；
“Q1 a b”，询问点a和点b是否在同一个连通块中，a和b可能相等；
“Q2 a”，询问点a所在连通块中点的数量；
输入格式
第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“C a b”，“Q1 a b”或“Q2 a”中的一种。

输出格式
对于每个询问指令”Q1 a b”，如果a和b在同一个连通块中，则输出“Yes”，否则输出“No”。

对于每个询问指令“Q2 a”，输出一个整数表示点a所在连通块中点的数量

每个结果占一行。

数据范围
1 ≤ n,m ≤ 10^5
输入样例：
5 5
C 1 2
Q1 1 2
Q2 1
C 2 5
Q2 5
输出样例：
Yes
2
3
"""
N = 10 ** 5
P = [0]
CNT = [1] * (N + 10)  # 当前连通块中的点


def get_root(x):
    if P[x] != x:
        P[x] = get_root(P[x])
    return P[x]


def merge(x, y):
    if get_root(x) != get_root(y):  # 如果 a,b已经在同一个集合中，则不需进行合并操作
        CNT[get_root(y)] += CNT[get_root(x)]
        P[get_root(x)] = get_root(y)


def query(x, y):
    return get_root(x) == get_root(y)


def query_count(x):
    return CNT[get_root(x)]


if __name__ == '__main__':
    n, m = map(int, input().split())
    P += [x for x in range(1, n + 1)]
    for i in range(m):
        op, *x = input().split()
        x = list(map(int, x))
        if op == 'C':
            merge(*x)
        elif op == 'Q1':
            print('Yes' if query(*x) else 'No')
        elif op == 'Q2':
            print(query_count(*x))
