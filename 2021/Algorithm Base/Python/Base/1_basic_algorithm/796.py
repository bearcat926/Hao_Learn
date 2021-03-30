"""
子矩阵的和
输入一个n行m列的整数矩阵，再输入q个询问，每个询问包含四个整数x1, y1, x2, y2，表示一个子矩阵的左上角坐标和右下角坐标。

对于每个询问输出子矩阵中所有数的和。

输入格式
第一行包含三个整数n，m，q。

接下来n行，每行包含m个整数，表示整数矩阵。

接下来q行，每行包含四个整数x1, y1, x2, y2，表示一组询问。

输出格式
共q行，每行输出一个询问的结果。

数据范围
1 ≤ n,m ≤ 1000,
1 ≤ q ≤ 200000,
1 ≤ x1 ≤ x2 ≤ n,
1 ≤ y1 ≤ y2 ≤ m,
−1000 ≤ 矩阵内元素的值 ≤ 1000
输入样例：
3 4 3
1 7 2 4
3 6 2 8
2 1 2 3
1 1 2 2
2 1 3 4
1 3 3 4
输出样例：
17
27
21
"""

N, M, Q = map(int, input().split())
int_matrix = []
for i in range(N):
    int_matrix.append(list(map(int, input().split())))

S = [[0] * (M + 1) for _ in range(N + 1)]  # int_matrix 从0开始计算位置，S从1开始计算位置，计算时int_matrix的坐标需要-1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + int_matrix[i - 1][j - 1]

for i in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    print(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1])
