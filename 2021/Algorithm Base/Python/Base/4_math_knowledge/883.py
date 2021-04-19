"""
高斯消元 O(n^3)

    对于形如
    {
        a11*x1 + a12*x2 + ... + a1n*xn = b1,
        a11*x1 + a12*x2 + ... + a1n*xn = b1,
        ...
        am1*x1 + am2*x2 + ... + amn*xn = bm
    }
    的方程组进行初等行列变换，以此求出方程组的解

    初等行列变换 - 不会改变方程的解(从对方程的操作理解)
        1. 把某一行乘一个非零的数
        2. 交换某两行
        3. 把某行的若干倍加到另一行

    通过初等行列变换，将线性方程组化简为形如下图的新方程组：
    {
        a11*x1 + a12*x2 + ... + a1n*xn = b1,
                 a12*x2 + ... + a1n*xn = b1,
        ...
                                    xn = bm
    }

    对结果的判断：
        1. 完美阶梯型 - 唯一解
        2. 0 = !0   - 无解
        3. 0 = 0    - 无穷多组解

    高斯消元的具体步骤：

        枚举每一列c
            1. 找到 c列绝对值最大的一行
            2. 将该行换到最上面去
            3. 将该行的第一个数变成 1
            4. 将下面所有行的第c列清成 0
            5. 处理下一列，循环直到最后一行只有一列为止
            6. 将最后一行c列的值带入之前一行，并将上面所有行的第c列清成 0
            7. 处理上一列，循环直到第一行只有一列为止
=============================================
高斯消元解线性方程组
输入一个包含 n 个方程 n 个未知数的线性方程组。

方程组中的系数为实数。

求解这个方程组。

下图为一个包含 m 个方程 n 个未知数的线性方程组示例：

{
    a11*x1 + a12*x2 + ... + a1n*xn = b1,
    a11*x1 + a12*x2 + ... + a1n*xn = b1,
    ...
    am1*x1 + am2*x2 + ... + amn*xn = bm
}

输入格式
第一行包含整数 n。

接下来 n 行，每行包含 n+1 个实数，表示一个方程的 n 个系数以及等号右侧的常数。

输出格式
如果给定线性方程组存在唯一解，则输出共 n 行，其中第 i 行输出第 i 个未知数的解，结果保留两位小数。

如果给定线性方程组存在无数解，则输出 Infinite group solutions。

如果给定线性方程组无解，则输出 No solution。

数据范围
1≤n≤100,
所有输入系数以及常数均保留两位小数，绝对值均不超过 100。

输入样例：
3
1.00 2.00 -1.00 -6.00
2.00 1.00 -3.00 -9.00
-1.00 -1.00 2.00 7.00
输出样例：
1.00
-2.00
3.00
"""
S = []
n = 0


def gaussian_elimination():
    global S
    r = 0
    for c in range(n):  # 处理第 c列 ∈ [0, n - 1]
        t = r
        for i in range(r, n):  # 找当前 c列值最大的行
            if abs(S[i][c]) > abs(S[t][c]):
                t = i
        if int(S[t][c]) == 0:  # c列值等于0
            continue
        S[r], S[t] = S[t], S[r]  # 交换两列
        r_c = S[r][c]
        S[r] = [S[r][x] / r_c for x in range(n + 1)]  # 处理行数据 x ∈ [0, n]
        for k in range(r + 1, n):  # 处理下面行
            r_c = S[k][c]
            S[k] = [S[k][x] for x in range(c)] + [S[k][x] - r_c * S[r][x] for x in range(c, n + 1)]
        r += 1  # 最上面的行下降一层

    r = n - 1
    for c in range(n - 1, -1, -1):  # 处理第 c列
        if round(S[r][c]) == 0:  # c列值等于0, 结果需要四舍五入判断
            print('Infinite group solutions' if round(S[r][n]) == 0 else 'No solution')  # 无穷多组解 :无解
            return
        r_c = S[r][c]
        S[r] = [S[r][x] / r_c for x in range(n + 1)]  # r_c变为 1
        for k in range(0, r):  # 处理上面行
            r_c = S[k][c]
            S[k] = [S[k][x] for x in range(c)] + [S[k][x] - r_c * S[r][x] for x in range(c, n + 1)]
        r -= 1  # 最下面的行上升一层

    for i in range(n):
        print(f'%.2f' % S[i][n])


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        S.append(list(map(float, input().split())))
    gaussian_elimination()
