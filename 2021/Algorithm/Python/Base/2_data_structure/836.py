"""
合并集合
一共有n个数，编号是1~n，最开始每个数各自在一个集合中。

现在要进行m个操作，操作共有两种：

“M a b”，将编号为a和b的两个数所在的集合合并，如果两个数已经在同一个集合中，则忽略这个操作；
“Q a b”，询问编号为a和b的两个数是否在同一个集合中；
输入格式
第一行输入整数n和m。

接下来m行，每行包含一个操作指令，指令为“M a b”或“Q a b”中的一种。

输出格式
对于每个询问指令”Q a b”，都要输出一个结果，如果a和b在同一集合内，则输出“Yes”，否则输出“No”。

每个结果占一行。

数据范围
1≤n,m≤10^5
输入样例：
4 5
M 1 2
M 3 4
Q 1 2
Q 1 3
Q 3 4
输出样例：
Yes
No
Yes


并查集

1. 讲两个集合合并
2. 询问两个元素是否在一个集合中

时间复杂度近乎O(1)


树形集合（不一定是二叉树）
    每个集合用一棵树来表示，树根的编号就是整个集合的编号。
    每个节点存储其父节点，即p[x]表示x的父节点。

    问题1：如何判断树根 => if p[x] = x:
    问题2：如何求x的集合编号 => while p[x] != x: x = p[x]
    问题3：如何合并两个集合 => 使Y集合的树根p[y] 成为 A集合树根p[x] 的一个子节点，则A集合成为新的合并集合 => p[y] = x

    对于问题2的优化：路径压缩
        在进行第一次求x的集合编号后，将x的所有祖先节点的父节点改为树根节点

         root
          o
        /  \
       o    o
     /  \  / \
    o   o o   o
"""
P = [0]


def get_root(x):  # 返回树根 + 路径压缩
    if P[x] != x:
        P[x] = get_root(P[x])
    return P[x]


def merge(x, y):
    P[get_root(x)] = get_root(y)  # 使x的树根的父节点 = y的树根


def query(x, y):
    return get_root(x) == get_root(y)  # 查看x的树根和y的树根是不是一个


if __name__ == '__main__':
    n, m = map(int, input().split())
    P += [x for x in range(1, n + 1)]
    for i in range(m):
        op, *x = input().split()
        x = list(map(int, x))
        if op == 'M':
            merge(*x)
        elif op == 'Q':
            print('Yes' if query(*x) else 'No')