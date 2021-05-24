"""
石子合并
设有 N 堆石子排成一排，其编号为 1，2，3，…，N。

每堆石子有一定的质量，可以用一个整数来描述，现在要将这 N 堆石子合并成为一堆。

每次只能合并相邻的两堆，合并的代价为这两堆石子的质量之和，合并后与这两堆石子相邻的石子将和新堆相邻，合并时由于选择的顺序不同，合并的总代价也不相同。

例如有 4 堆石子分别为 1 3 5 2， 我们可以先合并 1、2 堆，代价为 4，得到 4 5 2， 又合并 1，2 堆，代价为 9，得到 9 2 ，再合并得到 11，总代价为 4+9+11=24；

如果第二步是先合并 2，3 堆，则代价为 7，得到 4 7，最后一次合并代价为 11，总代价为 4+7+11=22。

问题是：找出一种合理的方法，使总的代价最小，输出最小代价。

输入格式
第一行一个数 N 表示石子的堆数 N。

第二行 N 个数，表示每堆石子的质量(均不超过 1000)。

输出格式
输出一个整数，表示最小代价。

数据范围
1 ≤ N ≤ 300
输入样例：
4
1 3 5 2
输出样例：
22
=====================================
状态表示 f(i)

    集合：所有将第i堆石子到第j堆石子合并成一堆石子的合并方式

    属性：MIN

状态计算

    f(i-1, j)，f(i, j-1)包含重复情况，原因是当前情况包含但不等于 必选 a[i]或b[j]的情况。
    但并不影响最终结果，因为题目求的值为 MAX

    f(i, j) = min(f(i, k) + f(k+1, j) + (S[j] - S[i-1]))
    其中 k ∈ [i, j-1]，因为右侧堆的最小情况为 k+1 = j
"""
N = 300 + 10
SUP = 10 ** 8
F = [[0] * N for i in range(N)]  # 需要全部初始化

if __name__ == '__main__':
    n = int(input())
    L = list(map(int, input().split()))
    # 前缀和处理
    S = [0]
    res = 0
    for i in range(len(L)):
        res += L[i]
        S.append(res)
    for length in range(2, n + 1):  # 区间长度为 1时，不需要合并，值都为自身
        for i in range(1, n - length + 1 + 1):
            l, r = i, i + length - 1
            F[l][r] = SUP  # 设当前 F[l][r]的值为一个上确界，便于进行最小资计算
            for k in range(l, r):
                F[l][r] = min(F[l][r], F[l][k] + F[k + 1][r] + (S[r] - S[l - 1]))
    print(F[1][n])
