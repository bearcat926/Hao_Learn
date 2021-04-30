"""
最长公共子序列
给定两个长度分别为 N 和 M 的字符串 A 和 B，求既是 A 的子序列又是 B 的子序列的字符串长度最长是多少。

输入格式
第一行包含两个整数 N 和 M。

第二行包含一个长度为 N 的字符串，表示字符串 A。

第三行包含一个长度为 M 的字符串，表示字符串 B。

字符串均由小写字母构成。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N,M≤1000
输入样例：
4 5
acbd
abedc
输出样例：
3
=====================================
状态表示 f(i)

    集合：所有在第一个序列的前 i个字母中出现，且在第二个序列的前 j个字母中出现的子序列

    属性：max

状态计算

    f(i, j) = max(f(i-1, j), f(i, j-1), f(i-1, j-1) + 1)

"""


if __name__ == '__main__':
    n, m = map(int, input().split())

