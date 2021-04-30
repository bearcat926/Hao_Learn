"""
n-皇后问题
n-皇后问题是指将 n 个皇后放在 n∗n 的国际象棋棋盘上，使得皇后不能相互攻击到，
即任意两个皇后都不能处于同一行、同一列或同一斜线上。

现在给定整数n，请你输出所有的满足条件的棋子摆法。

输入格式
共一行，包含整数n。

输出格式
每个解决方案占n行，每行输出一个长度为n的字符串，用来表示完整的棋盘状态。

其中”.”表示某一个位置的方格状态为空，”Q”表示某一个位置的方格上摆着皇后。

每个方案输出完成后，输出一个空行。

注意：行末不能有多余空格。

输出方案的顺序任意，只要不重复且没有遗漏即可。

数据范围
1≤n≤9
输入样例：
4
输出样例：
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..

"""
N = 9 + 1  # +1就不需要处理边界了
Board = [['.'] * N for i in range(N)]
# Col 代表行, [0, 9]; Row 代表列, [0, 9]
# DG - 正斜线; UDG - 反斜线,
Row, Col, DG, UDG = [False] * N, [False] * N, [False] * (2 * N), [False] * (2 * N)
n = 0


def check(y, x, n):  # 检查该点是否可用
    return (Row[y] is not True) and (Col[x] is not True) \
           and (DG[y + x] is not True) and (UDG[n - x + y] is not True)


def dfs(y, x, i):
    if x == n:  # 进位，纵轴坐标+1
        y += 1
        x = 0
        if y == n:  # 遍历完所有点
            if i == n:  # 检查皇后数量是否为n
                for a in range(0, n):
                    for b in range(0, n):
                        print(Board[a][b], end='')
                    print()
                print()
            return  # 不符合则返回

    dfs(y, x + 1, i)  # 该点不放皇后的情况

    if check(y, x, n):  # 检查该点是否可以放皇后
        Board[y][x] = 'Q'
        Row[y] = Col[x] = DG[y + x] = UDG[n - x + y] = True
        dfs(y, x + 1, i + 1)  # 该点放皇后的情况
        Row[y] = Col[x] = DG[y + x] = UDG[n - x + y] = False
        Board[y][x] = '.'


if __name__ == '__main__':
    n = int(input())
    dfs(0, 0, 0)
