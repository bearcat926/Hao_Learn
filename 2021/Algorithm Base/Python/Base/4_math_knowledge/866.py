"""
质数

    在大于 1 的整数中，如果只包含 1 和本身这两个约数，就称其质数，也叫素数。

    质数的判定 - 试除法：暴力O(n) -> 优化后O(√n)

        若 d | n =>  d 可以整除 n，即 n % d == 0
        则 n 具有两个除数 d1 <= d2，
        若我们只枚举较小的 d1,
        当 d1 = n / d2 时，
        则 d1 <= n / d1
          d1 ^ 2 <= n
        由于正整数开方符号不变，
        则 d1 <= √n
=======================================
试除法判定质数
给定 n 个正整数 ai，判定每个数是否是质数。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个正整数 ai。

输出格式
共 n 行，其中第 i 行输出第 i 个正整数 ai 是否为质数，是则输出 Yes，否则输出 No。

数据范围
1≤n≤100,
1≤ai≤2^31−1
输入样例：
2
2
6
输出样例：
Yes
No
"""


def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i <= x / i:  # math.sqrt(x)比较慢; i * i <= n 存在溢出风险
        if x % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input())
        print('Yes' if is_prime(x) else 'No')
