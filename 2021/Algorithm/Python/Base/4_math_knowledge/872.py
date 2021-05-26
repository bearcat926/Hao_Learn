"""
欧几里得算法 - 辗转相除法

    若 d|a, 且 d|b
    则 d|a+b => d|xa+yb
    因此 (a, b) => (b, a mod b)

    原理
        若 a > b, 且有 c使得 a mod b = a - cb
        又因为 d|a, d|-cb, 则 d|a-cb
        则 d|a mod b

    再由 (a, b) => (b, a mod b),
    进一步可得在进行k次(a, b) => (b, a mod b)后,
    可得 (a, b) = d
=======================================
最大公约数
给定 n 对正整数 ai,bi，请你求出每对数的最大公约数。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个整数对 ai,bi。

输出格式
输出共 n 行，每行输出一个整数对的最大公约数。

数据范围
1 ≤ n ≤ 105,
1 ≤ ai, bi ≤ 2×10^9
输入样例：
2
3 6
4 6
输出样例：
3
2
"""


def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a  # 当 b = 0时, a 和 0的最大公约数为a


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(gcd(a, b))