"""
集合-Nim游戏
给定 n 堆石子以及一个由 k 个不同正整数构成的数字集合 S。

现在有两位玩家轮流操作，每次操作可以从任意一堆石子中拿取石子，每次拿取的石子数量必须包含于集合 S，最后无法进行操作的人视为失败。

问如果两人都采用最优策略，先手是否必胜。

输入格式
第一行包含整数 k，表示数字集合 S 中数字的个数。

第二行包含 k 个整数，其中第 i 个整数表示数字集合 S 中的第 i 个数 si。

第三行包含整数 n。

第四行包含 n 个整数，其中第 i 个整数表示第 i 堆石子的数量 hi。

输出格式
如果先手方必胜，则输出 Yes。

否则，输出 No。

数据范围
1≤n,k≤100,
1≤si,hi≤10000
输入样例：
2
2 5
3
2 4 7
输出样例：
Yes
=====================================
博弈论

    有向图游戏

        给定一个有向无环图，图中有一个唯一的起点，在起点上放有一枚棋子。
        两名玩家交替地把这枚棋子沿有向边进行移动，每次可以移动一步.无法移动者判负，该游戏被称为有向图游戏。
        任何一个公平组合游戏都可以转化为有向图游戏。
        具体方法是，把每个局面看成图中的一个节点，并且从每个局面向沿着合法行动能够到达的下一个局面连有向边。

    Mex运算

        设 S表示一个非负整数集合，定义 mex(S)为求出不属于集合 S的最小非负整数的运算，
        即 mex(S) = min(x), x属于自然数，且x不属于S

    SG函数

        在有向图游戏中，对于每个节点 x，设从 x出发共有 k条有向边，分别到达节点 y1, y2 ... yk
        定义 SG(x)为 x的后继节点 y1, y2 ... yk的 SG函数值构成的集合再执行 mex(S)运算的结果，
        即 SG(x) = mex({SG(y1), SG(y2), ... , SG(yk)})
        特别地，整个有向图游戏 G的 SG函数值被定义为有向图游戏起点 s的 SG函数值，即SG(G) = SG(s)
        SG(end) = 0


    有向图游戏的和

        设G1, G2, ..., Gm是 m个有向图游戏，定义有向图游戏 G，它的行动规则是任选某个有向图游戏 Gi，
        并在 Gi上行动一步，G被称为有向图游戏 G1, G2, ..., Gm的和
        有向图游戏的和的 SG函数值等于它包含的各个子游戏 SG函数值的异或和
        即：SG(G) = SG(G1) ^ SG(G2) ^ ... ^ SG(Gm)


"""
N, M = 100 + 10, 10000 + 10
# S存储的是可供选择的集合, F存储的是所有可能出现过的情况的 SG值, 初始化 F均为 -1,方便查看 SG(x)是否被记录过
S, F = [], [-1] * M


def SG(x):
    # 因为取石子数目的集合 S是已经确定了的, 所以在递归条件下，每个数的 SG值也都是确定的, 如果F[x]已经存储过了, 直接返回即可
    if F[x] != -1:
        return F[x]
    SET = set()
    for i in range(k):
        _op = S[i]
        if x >= _op:  # 尝试当前 x值允许的操作
            SET.add(SG(x - _op))  # 先延伸到终点的 SG值后,再从后往前排查出所有数的 SG值

    i = 0
    while True:  # 循环完之后, 可以选出没有出现的最小自然数
        if not SET.__contains__(i):
            F[x] = i  # 对F[x]赋值
            return i
        i += 1


if __name__ == '__main__':
    k = int(input())  # 表示数字集合 S 中数字的个数
    S = list(map(int, input().split()))  # 数字集合 S 中的第 i 个数 si
    n = int(input())  # 整数 n
    H = list(map(int, input().split()))  # 第 i 堆石子的数量 hi

    res = 0
    for i in range(n):
        res ^= SG(H[i])  # 计算所有堆的异或值,基本原理与Nim游戏相同

    print('Yes' if res >= 1 else 'No')  # res != 0