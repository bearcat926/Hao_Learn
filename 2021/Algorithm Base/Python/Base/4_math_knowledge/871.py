"""
约数之和的计算

    根据唯一分解定理(算术基本定理), 一个合数N = P1^α1 * P2^α2 * ... * Pn^αn
    由此可得, Pn^αn 可以产生的不同结果为 Pn^0, ... , Pn^αn
    则 每个Pn^αn项产生结果和的乘积，即 (P1^0 + ... + P1^α1) * ... * (Pn^0 + ... + Pn^αn)
        的展开项 = 约数之和的累加项，所以约数之和 = (P1^0 + ... + P1^α1) * ... * (Pn^0 + ... + Pn^αn)
=======================================
约数之和
给定 n 个正整数 ai，请你输出这些数的乘积的约数之和，答案对 10^9+7 取模。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个整数 ai。

输出格式
输出一个整数，表示所给正整数的乘积的约数之和，答案需对 10^9+7 取模。

数据范围
1≤n≤100,
1≤ai≤2×10^9
输入样例：
3
2
6
8
输出样例：
252
"""
res = 1
mod = 10 ** 9 + 7
PRIME = {}


def get_divisor_num(x):
    global res
    i = 2
    while i <= x / i:
        if x % i == 0:
            PRIME[i] = PRIME[i] if PRIME.__contains__(i) else 0
            while x % i == 0:
                x //= i
                PRIME[i] += 1
        i += 1
    if x > 1:
        PRIME[x] = PRIME[x] + 1 if PRIME.__contains__(x) else 1


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input())
        get_divisor_num(x)
    for i in PRIME:
        r = 1
        while PRIME[i] != 0:
            r = (r * i + 1) % mod
            PRIME[i] -= 1
        res = res * r % mod
    print(res)

    """
        r0 = 1
        r1 = (r0 * i) + 1 => i + 1
        r2 = (r1 * i) + 1 => (i + 1) * i + 1 = i ^ 2 + i + 1
        ...
        rn = (rn-1 * i) + 1 => 1 + i + ... + i ^ n
        
        逆推证明：
            rn = i ^ n + ... + i + 1
               = i * (i ^ (n - 1) + ... + 1) + 1
               = i * (i * (i ^ (n - 2) + ... + 1) + 1) + 1
               ...
               当最里一层为 (i + 1)时，等式由n层形如 (exp(i ^ k) + i) 的表达式组成
               即从(i + 1)向外递归k次即可得到rk
    """
