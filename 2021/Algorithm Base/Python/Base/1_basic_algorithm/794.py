"""
高精度除法
给定两个非负整数A，B，请你计算 A / B的商和余数。

输入格式
共两行，第一行包含整数A，第二行包含整数B。

输出格式
共两行，第一行输出所求的商，第二行输出所求余数。

数据范围
1 ≤ A的长度 ≤ 100000,
1 ≤ B ≤ 10000
B 一定不为0

输入样例：
7
2
输出样例：
3
1
"""
A = list(map(int, input()))
B = int(input())


def div(s1, num):
    length = len(s1)

    s2 = []
    t = 0

    for i in range(length):
        div_num = s1[i] + t
        if div_num < num:
            s2.append(0)
            t = div_num * 10
        else:
            s2.append(div_num // num)
            t = (div_num % num) * 10

    s2.reverse()
    for i in range(length - 1, 0, -1):  # 去除前置0
        if s2[i] != 0:
            break
        s2.pop(i)
    s2.reverse()

    print(''.join(list(map(str, s2))))
    print(t // 10)


if __name__ == '__main__':
    div(A, B)
