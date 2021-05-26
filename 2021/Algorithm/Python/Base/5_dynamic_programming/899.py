"""
编辑距离
给定 n 个长度不超过 10 的字符串以及 m 次询问，每次询问给出一个字符串和一个操作次数上限。

对于每次询问，请你求出给定的 n 个字符串中有多少个字符串可以在上限操作次数内经过操作变成询问给出的字符串。

每个对字符串进行的单个字符的插入、删除或替换算作一次操作。

输入格式
第一行包含两个整数 n 和 m。

接下来 n 行，每行包含一个字符串，表示给定的字符串。

再接下来 m 行，每行包含一个字符串和一个整数，表示一次询问。

字符串中只包含小写字母，且长度均不超过 10。

输出格式
输出共 m 行，每行输出一个整数作为结果，表示一次询问中满足条件的字符串个数。

数据范围
1 ≤ n, m ≤ 1000,

输入样例：
3 2
abc
acd
bcd
ab 1
acbd 2
输出样例：
1
3
"""
N = 1000 + 10
F, STR = [[0] * N for x in range(N)], []


def edit_distance(A, B):
    ls, lt = len(A) - 1, len(B) - 1
    for i in range(ls + 1):
        F[i][0] = i
    for j in range(lt + 1):
        F[0][j] = j
    for i in range(1, ls + 1):
        for j in range(1, lt + 1):
            F[i][j] = min(F[i - 1][j] + 1, F[i][j - 1] + 1, F[i - 1][j - 1] + (1 if A[i] != B[j] else 0))
    return F[ls][lt]


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        STR.append([''] + list(map(str, input())))
    while m != 0:
        cnt = 0
        p = input().split()
        t, limit = [''] + list(str(p[0])), int(p[1])
        for i in range(len(STR)):
            if edit_distance(STR[i], t) <= limit:
                cnt += 1
        m -= 1
        print(cnt)