"""
快速幂求逆元
给定 n 组 ai,pi，其中 pi 是质数，求 ai 模 pi 的乘法逆元，若逆元不存在则输出 impossible。

注意：请返回在 0∼p−1 之间的逆元。

乘法逆元的定义
若整数 b，m 互质，并且对于任意的整数 a，如果满足 b|a，则存在一个整数 x，使得 a/b ≡ a*x(mod m)，
则称 x 为 b 的模 m 乘法逆元，记为 b^−1 (mod m)。
b 存在乘法逆元的充要条件是 b 与模数 m 互质。
当模数 m 为质数时，b^(m − 2) 即为 b 的乘法逆元。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个数组 ai,pi，数据保证 pi 是质数。

输出格式
输出共 n 行，每组数据输出一个结果，每个结果占一行。

若 ai 模 pi 的乘法逆元存在，则输出一个整数，表示逆元，否则输出 impossible。

数据范围
1 ≤ n ≤ 10^5,
1 ≤ ai, pi ≤ 2 * 10^9
输入样例：
3
4 3
8 5
6 3
输出样例：
1
2
impossible
=======================================
解法

    当 m为质数时，可以用快速幂求逆元：
        对 a / b ≡ a * x (mod m)
        两边同乘 b且同除 a可得 1 ≡ b * x (mod m)
        同 b * x ≡ 1 (mod m)
        由费马小定理可知，当 p为质数且 p|a不等价时, a ^ (p - 1) ≡ 1 (mod p)
        由于原式中 b，m 互质, 满足定理条件
        将 b, m带入定理
        可得 b ^ (m - 1) ≡ 1 (mod m)
        可分解左侧为 b * b ^ (m - 2) ≡ 1 (mod m)
        故当 m为质数时，b的乘法逆元 x = b ^ (m - 2)

    当n不是质数时，可以用扩展欧几里得算法求逆元：
        a有逆元的充要条件是 a, p互质，所以 gcd(a, p) = 1
        假设 a的逆元为x，那么有 a * x ≡ 1 (mod p)
        等价：ax + py = 1
        ex_gcd(a, p, x, y)
"""


def fermat_and_fast_power(a, p):  # a = a ^ (2 ^ 0)
    k, res = p - 2, 1
    # do ... while
    if k & 1 == 1:
        res = res * a % p  # res * a ^ (2 ^ t)
    a = a * a % p  # a ^ (2 ^ t) * a ^ (2 ^ t) = a ^ (a * 2 ^ t) = a ^ (2 ^ (t + 1))
    k >>= 1
    while k != 0:
        if k & 1 == 1:
            res = res * a % p
        a = a * a % p
        k >>= 1
    print(res if a % p != 0 and res > 0 else 'impossible')  # 可能会出现 p|a 等价的情况出现


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, p = map(int, input().split())
        fermat_and_fast_power(a, p)
