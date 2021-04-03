"""
求组合数 II
给定 n 组询问，每组询问给定两个整数 a，b，请你输出 C(a, b) mod (10^9+7) 的值。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一组 a 和 b。

输出格式
共 n 行，每行输出一个询问的解。

数据范围
1≤n≤10000,
1≤b≤a≤10^5
输入样例：
3
3 1
5 3
2 2
输出样例：
3
10
1
==============================================================
解决方法：

    预处理所有需要 [1, a]的阶乘和 [1, b]的阶乘逆元
"""

N = 10 ** 5 + 10
MOD = 10 ** 9 + 7
# 预处理阶乘结果和 a，b值对应逆元结果
FACT = [1]
INFACT = [1]


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
    return res  # 可能会出现 p|a 等价的情况出现


def init():
    for i in range(1, N):
        FACT.append((FACT[i - 1] * i) % MOD)
        # 因为 MOD 为质数，根据费马小定理可得 x = b ^ (m - 2) => INFACT[i] = i ^ (MOD - 2)
        INFACT.append((INFACT[i - 1] * fermat_and_fast_power(i, MOD)) % MOD)


if __name__ == '__main__':
    init()
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(((((FACT[a] * INFACT[b]) % MOD) * INFACT[a - b]) % MOD))  # C(a, b) = a! / (b! * (a - b)!)
