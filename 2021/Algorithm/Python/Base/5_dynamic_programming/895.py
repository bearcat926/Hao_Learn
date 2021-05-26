"""
最长上升子序列
给定一个长度为 N 的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数 N。

第二行包含 N 个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1 ≤ N ≤ 1000，
−10^9 ≤ 数列中的数 ≤ 10^9
输入样例：
7
3 1 2 1 8 5 6
输出样例：
4
=====================================
状态表示 f(i)

    集合：所有以第i个数结尾的上升子序列

    属性：max

状态计算

    f(i) = max(f(j) + 1), j = 0, 1, 2, ... , i-1

"""
N = 1000 + 10
F = [0] * N
G = [0] * N  # 求最长子序列

if __name__ == '__main__':
    n = int(input())
    L = [0] + list(map(int, input().split()))
    # dp
    res = 1
    for i in range(1, n + 1):
        F[i] = 1  # 从 L[i]开始，长度记为 1
        G[i] = 0
        for j in range(1, i + 1):  # [1, i]
            if L[j] < L[i]:  # 在以 i为结尾的序列中，由于之前的序列被计算过，因此当L[i] > L[j]时，长度+1
                # F[i] = max(F[i], F[j] + 1)
                if F[i] < F[j] + 1:
                    F[i] = F[j] + 1
                    G[i] = j  # 当前序列中，i的下一位为 j
        res = max(res, F[i])
    print(res)
    # 打印最长子序列
    k = 1
    for i in range(1, n + 1):  # 求最优解坐标
        if F[k] < F[i]:
            k = i
    l = F[k]
    for i in range(0, l):  # 打印为倒序序列
        print(L[k], end=' ')
        k = G[k]