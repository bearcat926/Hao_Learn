"""
多重背包问题 II
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N≤1000
0<V≤2000
0<vi,wi,si≤2000
提示：
本题考查多重背包的二进制优化方法。

输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
"""
"""
优化为二维
    
    不能用完全背包的优化思路来优化这个问题，因为每组的物品的个数都不一样，不能像之前一样推导:
    
    f(i, j)   = MAX(F[i-1][j], (F[i-1][j-V[i]]+w), (F[i-1][j-2*V[i]]+2*w), ..., F[i-1][j-s*V[i]]+s    *W[i])
    f(i, j-v) = MAX(            F[i-1][j-v]      , (F[i-1][j-  V[i]]+  w), ..., F[i-1][j-s*V[i]]+(s-1)*W[i], F[i-1][j-(s+1)*V[i]]+s*W[i])

优化为二进制 + 01背包
    
    对数量S打包分组为 2^0, 2^1, 2^2, ... , 2^k, C => C为按二进制分组之后的剩余部分
    并以此对V, W打包进行分组, 得到新的物品，且每个物品有且只有一件
    最终通过将多重背包转化为01背包问题的方式完成优化工作

"""
from math import log

N, M = 1000 * (int(log(2000, 2)) + 1 + 1), 2000 + 10
V, W = [0] * N, [0] * N
F = [0] * N

if __name__ == '__main__':
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n):
        v, w, s = map(int, input().split())
        k = 1  # 2^0
        while k <= s:
            cnt += 1
            V[cnt], W[cnt] = v * k, w * k
            s -= k
            k <<= 1
        if s > 0:  # 处理C
            cnt += 1
            V[cnt], W[cnt] = v * s, w * s
    n = cnt  # 更新n
    # dp
    for i in range(1, n + 1):  # [1, n]
        for j in range(m, V[i] - 1, -1):  # [m, V[i]]
            F[j] = max(F[j], F[j - V[i]] + W[i])
    print(F[m])
    print(cnt)
