"""
裴蜀定理

    有一对正整数a, b，若 a, b具有最大公约数(a, b),
    那么一定存在非零整数 x, y,
    使得 ax + by = (a, b)

扩展欧几里得算法

    当 b = 0 时
        由裴蜀定理 ax + by = (a, b)
        带入 b = 0可得 ax = a
        则 x = 1, y = 0

    当 b ≠ 0 时
        将裴蜀定理带入欧几里得算法
        可得 gcd(b, a % b) = gcd(a, b)
          bx’ + (a % b)y‘ = ax + by => x’, y'为下层中的 x, y在当前层中的映射
        由于 a % b = a - a // b * b => //为向下取整
        带入可得 bx’ + (a - a // b * b)y‘ = ax + by
        整理得 ay' + b(x' - (a // b)y') = ax + by
        所以当前层中的 x = y', y = x' - (a // b)y'

=======================================
扩展欧几里得算法

给定 n 对正整数 ai,bi，对于每对数，求出一组 xi,yi，使其满足 ai×xi + bi×yi = gcd(ai,bi)。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含两个整数 ai,bi。

输出格式
输出共 n 行，对于每组 ai,bi，求出一组满足条件的 xi,yi，每组结果占一行。

本题答案不唯一，输出任意满足条件的 xi,yi 均可。

数据范围
1≤n≤105,
1≤ai,bi≤2×109
输入样例：
2
4 6
8 18
输出样例：
-1 1
-2 1
"""
x, y = 0, 0


def ex_gcd(a, b):
    global x, y
    if b == 0:
        x, y = 1, 0
        return a

    d = ex_gcd(b, a % b)  # 欧几里何核心 - 递归求最大公约数
    x, y = y, x - a // b * y  # 计算下一层的 x和 y, 但需要放在递归函数后，不然 x和 y的值会被改变
    return d


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        x, y = 0, 0
        ex_gcd(a, b)
        print(x, y)