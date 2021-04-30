"""
中国剩余定理 - 孙子定理

    解一元线性同余方程组 S = {x ≡ a1 mod (m1), x ≡ a2 mod (m2), ... , x ≡ an mod (mn)}

    假设整数m1, m2, ... , mn两两互质，则对任意的整数：a1, a2, ... , an，
    方程组 S有解，且通解可用如下方法构造：

    设 M = m1 * m2 * ... * mn, 并设 Mi = M / mi, (i ∈ [1, n]) 是除了 mi以外的 n - 1个整数的乘积。
    设 ti = Mi ^ -1 为 Mi 模 mi 意义下的逆元，所以 Mi * ti ≡ 1 (mod mi), (i ∈ [1, n])
    方程组的通解形式为 x = ∑(i ∈ [1, n]) ai * ti * Mi + kM
    在模M的意义下，方程组 S只有一个解：x = ∑(i ∈ [1, n]) ai * ti * Mi mod M

    证明

        假设可知，对任何 i ∈ [1, n]，都存在当 j != i时，(mi, mj) = 1
        由此可得 (mi, Mi) = 1
        这说明存在整数 ti使得 ti * Mi ≡ 1 (mod mi)
        两边同乘 ai得 ai * ti * Mi ≡ ai (mod mi)

        因此对 x = a1 * t1 * M1 + a2 * t2 * M2 + ... + an * tn * Mn
        满足 对任何 i ∈ [1, n]，x = ai * ti * Mi + ∑(j != i) aj * tj * Mj ≡ ai (mod mi)
        说明 x为方程组 S的一个解

        假设 x1和 x2都是方程组 S的解，那么 对任何 i ∈ [1, n]，存在 x1 - x2 ≡ 0 (mod mi)
        原因：x1 - x2 = a1 * t1 * M1 - a2 * t2 * M2
                     = a1 * t1 * (M1/mi) * mi - a2 * t2 * (M2/mi) * mi
                     ≡ 0 (mod mi)
        而 m1, m2, ... , mn两两互质，这说明 M | x1 - x2, 所以方程组 S的任何两个解之间必然相差 M的整数倍
        结合之前的x，方程组 S的所有解的集合为 x = ∑(i ∈ [1, n]) ai * ti * Mi + KM  (k ∈ Z)

    实现过程

        x ≡ mi (mod ai)
        可得 x mod ai = mi
        等同于 x = ki * ai + mi
        因此 i, j ∈ [1, n] 且 i ≠ j
        可得 ki * ai + mi = kj * aj + mj
            ki * ai + kj * (-aj) = mj - mi
        根据裴蜀定理 ax + by = gcd(a, b)
        可得 ki' * ai + kj' * (-aj) = gcd(ai, -aj)
        可推出结论 当 mj - mi 为 (ai, -aj) 整数倍时，等式有解

        设 d = gcd(ai, -aj), q = (mj − mi) / d
        因此 ki = ki' * q
        带入得 ki * ai + kj * (-aj) = q * d
        根据二元一次方程式通解 {x = x0 + bk/(a, b), y = y0 - ak/(a, b)}
        由此得 ki', kj'通解为 {ki = ki_0 + (-aj)*k/d, kj = kj_0 - ai*k/d}
        带入得 (ki_0 - aj*k/d) * ai + (kj_0 - ai*k/d) * (-aj) = q * d
        整理得 ki_0 * ai + kj_0 * (-aj) = q * d, 同样成立

        因此为使得 x具有最小非负整数，
        只需使得 {ki = ki_0 + (-aj)*k/d, kj = kj_0 - ai*k/d} 具有最小解
        即 ki = ki_0 % abs(aj/d)   => 不知道ai/d的正负性
          kj = kj_0 % abs(ai/d)

        带入 x = ki * ai + mi
        得 x = ki * ai + mi + ai * aj * k/d
        其中 ai * aj / d 为一个定值，在此设为 a,
        ki_0 为特值，因此 ki_0 * ai + mi 也为一个定值，在此设为 m
        因此 x = k * a + m
        该式与 x = ki * ai + mi结构近似，为两式合并后的结果

        因为 k = 0时，x为最小非负整数，
        因此 min(x) = m


=======================================
表达整数的奇怪方式
给定 2n 个整数 a1,a2,…,an 和 m1,m2,…,mn，求一个最小的非负整数 x，满足 ∀i∈[1,n],x ≡ mi(mod ai)。

输入格式
第 1 行包含整数 n。

第 2…n+1 行：每 i+1 行包含两个整数 ai 和 mi，数之间用空格隔开。

输出格式
输出最小非负整数 x，如果 x 不存在，则输出 −1。
如果存在 x，则数据保证 x 一定在 64 位整数范围内。

数据范围
1 ≤ ai ≤ 2 ^ 31−1,
0 ≤ mi < ai
1 ≤ n ≤ 25
输入样例：
2
8 7
11 9
输出样例：
31
"""
ki, kj = 0, 0


def ex_gcd(a, b):
    global ki, kj
    if b == 0:
        ki, kj = 1, 0
        return a

    d = ex_gcd(b, a % b)
    ki, kj = kj, ki - a // b * kj

    return d


def mod(a, b):  # 解决负数模
    return ((a % b) + b) % b


if __name__ == '__main__':
    n = int(input())
    has_answer = True
    ai, mi = map(int, input().split())
    aj, mj = 0, 0
    for i in range(n - 1):
        aj, mj = map(int, input().split())
        d = ex_gcd(ai, -aj)  # 负数的最大公约数要取绝对值
        if (mj - mi) % d != 0:
            has_answer = False
            break
        q = (mj - mi) // d
        ki = mod(ki * q, abs(aj // d))
        # x = ki * ai + mi + k * (ai * aj / d)
        mi, ai = ki * ai + mi, abs(ai * aj // d)
    print(mi if has_answer else -1)
