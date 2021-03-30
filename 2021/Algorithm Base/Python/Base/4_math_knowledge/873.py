"""
欧拉函数

    定义

        1∼N 中与 N 互质的数的个数被称为欧拉函数，记为 ϕ(N)。

    公式

        若在算数基本定理中，N = p1^a1 * p2^a2 * ... * pk^ak
        则：ϕ(N) = N * (1 − 1/p1) * (1 − 1/p2) * ... * (1 − 1/pk)

    证明

        容斥原理证明欧拉函数

            1. 先从1 ~ N中去掉从 p1 ~ pk 所有的倍数
            2. 加上所有 pi * pj 的倍数 (因为之前减了两次)
            3. 减去所有 pi * pj * pk 的倍数 (因为之前减了三次, 又加了三次，没加没减)
            4. 以此类推，减去奇数个质数的倍数，并加上偶数个质数的倍数就是最后结果

=======================================
给定 n 个正整数 ai，请你求出每个数的欧拉函数。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个正整数 ai。

输出格式
输出共 n 行，每行输出一个正整数 ai 的欧拉函数。

数据范围
1≤n≤100,
1≤ai≤2×10^9
输入样例：
3
3
6
8
输出样例：
2
2
4
"""
n = 0


def euler(x):
    res = x
    i = 2
    while i <= x / i:
        if x % i == 0:
            res -= res // i  # int(res * (1 - 1 / x))
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        res -= res // x
    print(res)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        euler(int(input()))
