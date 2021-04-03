"""
求组合数 IV
输入 a,b，求 C(a, b) 的值。

注意结果可能很大，需要使用高精度计算。

输入格式
共一行，包含两个整数 a 和 b。

输出格式
共一行，输出 C(a, b) 的值。

数据范围
1≤b≤a≤5000
输入样例：
5 3
输出样例：
10
==============================================================
解决方法：

    由于结果过大，所以在计算阶乘的时候需要使用高精度乘法和除法
    不过可以通过对阶乘分解质因数的方式略去除法部分
    详细过程如下：

        通过分解质因数，使 C(a, b) = p1^t1 + p2^t2 + ... + pk^tk
        因为a的阶乘中包含的 p的个数 num(a!, p) = (⌊a / p^1⌋ + ⌊a / p^2⌋ + ... + ⌊a / p^k⌋)
        因为 C(a, b)的结果为整数
        因此 对 a! / b!(a-b)! = ∏ p∈prime(a) p ^ (num(a!, p)-num(b!, p)-num((a-b)!, p))
        prime(a) 为 1~a中的所有质数
"""
N = 5000 + 10
PRIME, ST, cnt = [0] * N, [False] * N, 0
S = [0] * N


def get_num(a, p):
    res = 0
    while a != 0:
        res += a // p
        a //= p
    return res


def get_prime(n):
    global cnt
    i = 2
    while i <= n:
        if not ST[i]:  # 质数
            PRIME[cnt] = i
            cnt += 1
        j = 0
        while PRIME[j] <= n / i:
            ST[PRIME[j] * i] = True  # 只用最小值因子筛去合数
            if i % PRIME[j] == 0:  # 保持线性
                break
            j += 1
        i += 1


def mul(s1, num):
    s1.reverse()
    s2 = []
    t = 0
    for i in range(len(s1)):
        res = t + s1[i] * num
        t = res // 10
        s2.append(res % 10)

    if t != 0:
        s2.append(t)

    s2.reverse()
    return s2


if __name__ == '__main__':
    a, b = map(int, input().split())

    get_prime(a)  # 对a分解质因数
    for i in range(cnt):
        p = PRIME[i]
        S[i] = get_num(a, p) - get_num(b, p) - get_num(a - b, p)

    R = [1]
    for i in range(cnt):
        if S[i] * PRIME[i] != 0:
            R = mul(R, PRIME[i] ** S[i])

    print(''.join(list(map(str, R))))
