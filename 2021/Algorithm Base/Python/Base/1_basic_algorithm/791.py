"""
高精度加法
给定两个正整数，计算它们的和。

输入格式
共两行，每行包含一个整数。

输出格式
共一行，包含所求的和。

数据范围
1 ≤ 整数长度 ≤ 100000
输入样例：
12
23
输出样例：
35
"""
A = list(map(int, input()))
B = list(map(int, input()))


def add(s1, s2):
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
        res = s1[i] + s2[i] + t
        t = 0 if res < 10 else 1  # 检查进位
        s3.append(res % 10)  # 添加值

    if t == 1:  # 加法完成后，检查是否还需进位
        s3.append(1)

    s3.reverse()
    return s3


print(''.join(list(map(str, add(A, B)))))
