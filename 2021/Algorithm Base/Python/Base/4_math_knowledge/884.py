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
1≤n≤100
输入样例：
3
1 1 0 1
0 1 1 0
1 0 0 1
输出样例：
1
0
0
"""