"""
数的三次方根
给定一个浮点数n，求它的三次方根。

输入格式
共一行，包含一个浮点数n。

输出格式
共一行，包含一个浮点数，表示问题的解。

注意，结果保留6位小数。

数据范围
−10000 ≤ n ≤ 10000
输入样例：
1000.00
输出样例：
10.000000
"""

n = float(input())


def bsearch(l, r):
    while r - l > 1e-8:             # 浮点数二分法的循环条件是r-l<1e-8,其中8是因为题目中要保留6位小数
        mid = float((l + r) / 2)
        if mid * mid * mid >= n:
            r = mid
        else:
            l = mid
    return l


l = bsearch(-10000, 10000)
print("{:.6f}".format(l))
