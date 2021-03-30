"""
高精度乘法
给定两个正整数A和B，请你计算A * B的值。

输入格式
共两行，第一行包含整数A，第二行包含整数B。

输出格式
共一行，包含A * B的值。

数据范围
1 ≤ A的长度 ≤ 100000,
0 ≤ B ≤ 10000
输入样例：
2
3
输出样例：
6
"""
A = list(map(int, input()))
B = int(input())


def check_zero(s1, s2):
    if s2 == 0:
        return True
    if len(s1) == 1 and s1[0] == 0:
        return True
    return False


def mul(s1, num):
    length = len(s1)

    s1.reverse()

    s2 = []
    t = 0

    for i in range(length):
        res = t + s1[i] * num
        t = res // 10
        s2.append(res % 10)

    if t != 0:
        s2.append(t)

    s2.reverse()
    return s2


if __name__ == '__main__':
    if check_zero(A, B):
        print(0)
    else:
        print(''.join(list(map(str, mul(A, B)))))
