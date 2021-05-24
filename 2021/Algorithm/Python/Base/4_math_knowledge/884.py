"""
高斯消元解异或线性方程组
输入一个包含 n 个方程 n 个未知数的异或线性方程组。

方程组中的系数和常数为 0 或 1，每个未知数的取值也为 0 或 1。

求解这个方程组。

异或线性方程组示例如下：

M[1][1]x[1] ^ M[1][2]x[2] ^ … ^ M[1][n]x[n] = B[1]
M[2][1]x[1] ^ M[2][2]x[2] ^ … ^ M[2][n]x[n] = B[2]
…
M[n][1]x[1] ^ M[n][2]x[2] ^ … ^ M[n][n]x[n] = B[n]
其中 ^ 表示异或(XOR)，M[i][j] 表示第 i 个式子中 x[j] 的系数，B[i] 是第 i 个方程右端的常数，取值均为 0 或 1。

输入格式
第一行包含整数 n。

接下来 n 行，每行包含 n+1 个整数 0 或 1，表示一个方程的 n 个系数以及等号右侧的常数。

输出格式
如果给定线性方程组存在唯一解，则输出共 n 行，其中第 i 行输出第 i 个未知数的解。

如果给定线性方程组存在多组解，则输出 Multiple sets of solutions。

如果给定线性方程组无解，则输出 No solution。

数据范围
1 ≤ n ≤ 100
输入样例：
3
1 1 0 1
0 1 1 0
1 0 0 1
输出样例：
1
0
0
=============================================
异或 => 不进位加法

    对结果的判断：
        1. 完美阶梯型 - 唯一解
        2. 有矛盾    - 无解
        3. 无矛盾    - 无穷多组解

    高斯消元的具体步骤：

        枚举每一列c
            1. 枚举列
            2. 非零行
            3. 交换
            4. 下面清零



"""
S = []
n = 0


def gaussian_elimination():
    global S
    r = 0
    for c in range(n):  # 枚举列
        t = r
        # 找到非零的一行
        for i in range(r, n):
            if S[i][c] != 0:
                t = i
                break
        if S[t][c] == 0:  # 该列全为0
            continue
        # 交换两列
        S[t], S[r] = S[r], S[t]
        # 下面清零
        for k in range(r + 1, n):
            if S[k][c] != 0:
                S[k] = [S[k][x] for x in range(c)] + [S[k][x] ^ S[r][x] for x in range(c, n + 1)]
        r += 1  # 最上面的行下降一层

    if r < n:  # 消元过程中跳行了
        for i in range(r, n):
            if round(S[i][n]) != 0:  # 末尾不等于0
                print('No solution')  # 无解
                return
        print('Multiple sets of solutions')  # 无穷多组解
        return

    for c in range(n - 1, -1, -1):  # 处理第 c列
        for k in range(0, c):  # 消除上面行
            if S[k][c] != 0:
                S[k] = [S[k][x] for x in range(c)] + [S[k][x] ^ S[c][x] for x in range(c, n + 1)]

    for i in range(n):
        print(S[i][n])


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        S.append(list(map(int, input().split())))
    gaussian_elimination()