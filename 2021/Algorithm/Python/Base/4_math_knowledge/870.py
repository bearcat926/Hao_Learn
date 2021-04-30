"""
约数个数的计算

    根据唯一分解定理(算术基本定理), 一个合数N = P1^α1 * P2^α2 * ... * Pn^αn
    由此可得, Pn^αn 可以产生的不同结果为 Pn^0, ... , Pn^αn, 共(αn + 1)个
    则 每个Pn^αn项产生结果数的乘积, 即 (α1 + 1) * (α2 + 1) * ... *(αn + 1)
       的展开项 = 约数个数的累加项，所以约数个数 = (α1 + 1) * (α2 + 1) * ... *(αn + 1)
=======================================
约数个数
给定 n 个正整数 ai，请你输出这些数的乘积的约数个数，答案对 10^9+7 取模。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个整数 ai。

输出格式
输出一个整数，表示所给正整数的乘积的约数个数，答案需对 10^9+7 取模。

数据范围
1≤n≤100,
1≤ai≤2×10^9
输入样例：
3
2
6
8
输出样例：
12
"""
res = 1
mod = 10 ** 9 + 7
PRIME = {}


global res
def get_divisor_num(x):
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
        res = (res * (PRIME[i] + 1)) % mod
    print(res)
