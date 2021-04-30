"""
高精度减法
给定两个正整数，计算它们的差，计算结果可能为负数。

输入格式
共两行，每行包含一个整数。

输出格式
共一行，包含所求的差。

数据范围
1 ≤ 整数长度 ≤ 10^5
输入样例：
32
11
输出样例：
21
"""
A = list(map(int, input()))
B = list(map(int, input()))


def cmp(s1, s2):
    if len(s1) != len(s2):
        return len(s1) >= len(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[i] > s2[i]
    return True  # 相等


def sub(s1, s2):
    length = max(len(s1), len(s2))

    s1.reverse()
    s2.reverse()

    while length - len(s1) > 0:
        s1.append(0)

    while length - len(s2) > 0:
        s2.append(0)

    s3 = []
    t = 0

    for i in range(length):
        res = t + s1[i] - s2[i]
        t = -1 if res < 0 else 0
        s3.append(res + 10 if res < 0 else res)

    for i in range(length - 1, 0, -1):  # 去除前置0
        if s3[i] != 0:
            break
        s3.pop(i)
    s3.reverse()

    return s3


if __name__ == '__main__':
    if cmp(A, B):
        print(''.join(list(map(str, sub(A, B)))))
    else:
        print('-' + ''.join(list(map(str, sub(B, A)))))
