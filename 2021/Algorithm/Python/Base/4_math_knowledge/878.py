"""
线性同余方程

    形如 ai × xi ≡ bi(mod mi) 的方程
    存在y ∈ Z,使得 ai × x = mi × y + bi
    整理后可得 ai × x - mi × y = bi
    且 y ∈ Z, 可使得 -mi × y = mi × y'
    带入可得等式1 ai × x + mi × y = bi
    引入裴蜀定理,
    则当且仅当 ai, mi具有最大公约数(ai, mi)时, ai * x + mi * y = (ai, mi)
    对等式1两边同乘 bi / (ai, mi), 得 ai * bi / (ai, mi) * x + mi * bi / (ai, mi) * y = bi
    整理得 ai * bi / (ai, mi) * x = bi + mi * bi / (ai, mi) * y
    由 mi * bi / (ai, mi) * y mod mi == 0
    可得 ai * bi / (ai, mi) * x ≡ bi mod mi
    则 ai × xi ≡ ai * bi / (ai, mi) * x mod mi
    两边消去ai得 xi ≡ (bi / (ai, mi) * x) mod mi
    因此存在 (bi / (ai, mi) * x) mod mi 满足 xi

=======================================
线性同余方程
给定 n 组数据 ai,bi,mi，对于每组数求出一个 xi，使其满足 ai × xi ≡ bi(mod mi)，如果无解则输出 impossible。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含一组数据 ai,bi,mi。

输出格式
输出共 n 行，每组数据输出一个整数表示一个满足条件的 xi，如果无解则输出 impossible。

每组数据结果占一行，结果可能不唯一，输出任意一个满足条件的结果均可。

输出答案必须在 int 范围之内。

数据范围
1≤n≤105,
1≤ai,bi,mi≤2×109
输入样例：
2
2 3 6
4 3 5
输出样例：
impossible
-3

"""
x, y = 0, 0


def ex_gcd(i, j):
    global x, y
    if j == 0:
        x, y = 1, 0
        return i

    d = ex_gcd(j, i % j)
    x, y = y, x - i // j * y
    return d


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b, m = map(int, input().split())
        x, y = 0, 0
        d = ex_gcd(a, m)
        print((x * b // d) % m if b % d == 0 else 'impossible')
