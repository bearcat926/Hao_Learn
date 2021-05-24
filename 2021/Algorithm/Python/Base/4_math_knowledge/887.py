"""
求组合数 III

给定 n 组询问，每组询问给定两个整数 a，b，请你输出 C(a, b) mod p 的值。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一组 a,b,p。

输出格式
共 n 行，每行输出一个询问的解。

数据范围
1 ≤ n ≤ 20,
1 ≤ b ≤ a ≤ 10^18,
1 ≤ p ≤ 10^5,

输入样例：
3
5 3 7
3 1 5
6 4 13
输出样例：
3
3
2
==============================================================
解决方法：

    卢卡斯定律 - Lucas

        将 a, b 分别写为 p进制数
        即 a = ak * p^k + (ak-1) * p^(k-1) + ... + a0 * p^0 , ①
          b = bk * p^k + (bk-1) * p^(k-1) + ... + b0 * p^0 , ②
        因此 C(a, b) = C(ak, bk) * C(ak-1, bk-1) * ... * C(a0, b0) (mod p)

        按照递归角度考虑
        C(a, b)(lucas) ≡ C(a // p, b // p)(lucas) * C(a mod p, b mod p) (mod p)
        此处注意是 ⌊a / p⌋, 需要向下取整

        证明

            根据二项式定理展开式 (1+x)^p = C(p, 0) * x^0 + C(p, 1) * x^1 + ... + C(p, p-1) * x^(p-1) + C(p, p) * x^p
            由于 p为质数, 因此 (1+x)^p ≡ 1+x^p (mod p), ③

            将上述结论①, ③结合
            可得 (1+x)^a = (1+x)^(a0 * p^0 + a1 * p^1 + ... + ak * p^k)
                        = ((1+x)^(p^0))^a0 * ((1+x)^(p^1))^a1 * ... * ((1+x)^(p^k))^ak
                        = (1+x)^a0 * ((1+x)^(p^1))^a1 * ... * ((1+x)^(p^k))^ak
                        = (1+x)^a0 * (1+x^(p^1))^a1 * ... * (1+x^(p^k))^ak (mod p)
            设 (1+x)^n = (1+x)^(a*p+b)
                      ≡ (1+x^p)^a * (1+x)^b (mod p)
            根据二项式定理 (a+b)^n = ∑(0,n) C(n, i) a^(n-i) b^i
            可得 (1+x^p)^a * (1+x)^b = ∑(0,a) C(a, i) x^(p*i) * ∑(0,b) C(b, j) x^j
            因此 (1+x)^n ≡ ∑(0,a) C(a, i) x^(p*i) * ∑(0,b) C(b, j) x^j (mod p)
            对于 x^m项而言
            C(n, m) x^m ≡ C(a, i) C(b, j) x^(p*i+j) (mod p)
            因为 n = a * p + b, m = p * i + j
            可得 a = n // p, b = n % p, i = m // p, j = m % p
            因此 C(n, m) ≡ C(n // p, m // p) C(n % p, m % p) (mod p)
"""


def qmi(a, p):  # a = a ^ (2 ^ 0)
    k, res = p - 2, 1
    # do ... while
    while k != 0:
        if k & 1 == 1:
            res = res * a % p  # res * a ^ (2 ^ t)
        a = a * a % p  # a ^ (2 ^ t) * a ^ (2 ^ t) =  a ^ (2 ^ t + 2 ^ t) = a ^ (2 ^ t * 2) = a ^ (2 ^ (t + 1))
        k >>= 1
    return res  # 可能会出现 p|a 等价的情况出现


def C(a, b, p):  # C(a, b) = (a * (a-1) * ... * (a - (b - 1))) / (1 * 2 * ... * b)
    res = 1
    i, j = 1, a
    while i <= b:
        res = res * j % p
        res = res * qmi(i, p) % p
        i += 1
        j -= 1
    return res


def lucas(a, b, p):
    if a < p and b < p:
        return C(a, b, p)
    # 由于 a // p和 b // p的值可能会非常大, 因此需要继续使用 lucas进行化简直到可以计算
    return (C(a % p, b % p, p) * lucas(a // p, b // p, p)) % p


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b, p = map(int, input().split())
        print(lucas(a, b, p))
