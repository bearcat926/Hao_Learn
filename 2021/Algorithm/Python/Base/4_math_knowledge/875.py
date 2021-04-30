"""
同余定理

    欧拉定理

        若 a 与 n 互质, 即(a,m) = 1, 则 a^ϕ(n) ≡ 1 (mod n)

        证明
            在 1 ~ n中, 存在与n互质的数 p1, p2, ... , pϕ(n), 则 p1 * p2 * ... * pϕ(n) mod n = 1
            若 a 也与 n 互质, 则 a mod n = 1  =>  a^ϕ(n) mod n = 1
            因此 a^ϕ(n) * p1 * p2 * ... * pϕ(n) ≡ p1 * p2 * ... * pϕ(n) (mod n)
            两边同除 p1 * p2 * ... * pϕ(n), 可得 a^ϕ(n) ≡ 1 (mod n)

    费马小定理

        若 p为质数且 p|a不等价, 则 a^p ≡ a (mod p), 即 a^(p-1) ≡ 1 (mod p)

        证明

            由于 p为质数且 p|a不等价, 可推出 a与 n 互质
            则由欧拉定理结论可得, a^ϕ(p) ≡ 1 (mod p)
            因为p为质数, 则ϕ(p) = p - 1
            带入等式可得 a^(p-1) ≡ 1 (mod p)
            两边同乘a可得, a^p ≡ a (mod p)

=======================================
快速幂

    1. 预处理 a ^ (2 ^ k) mod p, 其中 k ∈ [0, log_k], 将其放入数组R中
    2. 为使得 a ^ k  ≡ a ^ (x0 + x1 + ... + xt) (mod p), 其中 xt 为 2^t
        只需使得 k = x0 + x1 + ... + xt
        带入等式得 a ^ k = a ^ (x0 + x1 + ... + xt)
                       = a ^ x0 * a ^ x1 * ... * a ^ xt
                       = R[0] * R[1] * ... * R[t]
        因此只需要计算出 R[0] * R[1] * ... * R[t] 的结果再 mod p 就可得出最后的结果

=======================================
快速幂
给定 n 组 ai,bi,pi，对于每组数据，求出 ai^bi mod pi 的值。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含三个整数 ai,bi,pi。

输出格式
对于每组数据，输出一个结果，表示 ai^bi mod pi 的值。

每个结果占一行。

数据范围
1 ≤ n ≤ 100000,
1 ≤ ai, bi, pi ≤ 2 * 10^9
输入样例：
2
3 2 5
4 3 9
输出样例：
4
1
"""
N = 2 * (10 ** 9)


def fast_power(a, b, p):
    res = 1
    # do ... while
    if b & 1 == 1:
        res = res * a % p  # res * a ^ (2 ^ t)
    a = a * a % p  # a ^ (2 ^ t) * a ^ (2 ^ t) = a ^ (2 * 2 ^ t) = a ^ (2 ^ (t + 1))
    b >>= 1
    while b != 0:
        if b & 1 == 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    print(res)


if __name__ == '__main__':
    x = 1
    n = int(input())
    for i in range(n):
        a, b, p = map(int, input().split())
        fast_power(a, b, p)