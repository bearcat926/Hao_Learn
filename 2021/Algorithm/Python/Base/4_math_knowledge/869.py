"""
约数

    试除法求一个数的所有约数 O(√n)

=======================================
试除法求约数
给定 n 个正整数 ai，对于每个整数 ai，请你按照从小到大的顺序输出它的所有约数。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一个整数 ai。

输出格式
输出共 n 行，其中第 i 行输出第 i 个整数 ai 的所有约数。

数据范围
1≤n≤100,
2≤ai≤2×109
输入样例：
2
6
8
输出样例：
1 2 3 6
1 2 4 8
"""
S = ()


def get_divisors(x):
    global S
    i = 1
    while i <= x / i:
        if x % i == 0:
            S.append(i)
            if i != x // i:  # i^2 != n， 则 i和 n / i是 n的一对约数
                S.append(x // i)
        i += 1
    S = sorted(S)
    for i in S:
        print(i, end=' ')
    print()


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input())
        S = []
        get_divisors(x)
