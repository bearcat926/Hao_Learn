"""
八数码
在一个3×3的网格中，1~8这8个数字和一个“x”恰好不重不漏地分布在这3×3的网格中。

例如：

1 2 3
x 4 6
7 5 8
在游戏过程中，可以把“x”与其上、下、左、右四个方向之一的数字交换（如果存在）。

我们的目的是通过交换，使得网格变为如下排列（称为正确排列）：

1 2 3
4 5 6
7 8 x
例如，示例中图形就可以通过让“x”先后与右、下、右三个方向的数字交换成功得到正确排列。

交换过程如下：

1 2 3   1 2 3   1 2 3   1 2 3
x 4 6   4 x 6   4 5 6   4 5 6
7 5 8   7 5 8   7 x 8   7 8 x
现在，给你一个初始网格，请你求出得到正确排列至少需要进行多少次交换。

输入格式
输入占一行，将3×3的初始网格描绘出来。

例如，如果初始网格如下所示：
1 2 3

x 4 6

7 5 8

则输入为：1 2 3 x 4 6 7 5 8

输出格式
输出占一行，包含一个整数，表示最少交换次数。

如果不存在解决方案，则输出”-1”。

输入样例：
2  3  4  1  5  x  7  6  8
输出样例
19

状态表示

    1. 还原
    2. 移动
    3. 转换


"""


class queue:
    def __init__(self, size):
        self.D = [0] * size
        self.head = -1
        self.tail = -1

    def empty(self):
        return self.head == self.tail

    def push(self, e):
        if self.tail < len(self.D):
            self.tail += 1
            self.D[self.tail] = e

    def pop(self):
        if not self.empty():
            self.head += 1
            return self.D[self.head]

    def query(self):
        if not self.empty():
            return self.D[self.head + 1]


N = 3
Q = queue(N ** (N * N + 3))  # 队列大小需要根据样例进行调整
M = {}  # 状态对应移动步数
S = set()  # 判断当前状态是否被处理过


def find(R):
    for i in range(len(R)):
        if R[i] == 'x':
            return i


def bfs(start):
    end = '12345678x'

    Q.push(start)
    M[start] = 0

    # 上右下左
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while Q.empty() is not True:
        t = Q.pop()

        if t == end:  # success
            print(M[t])
            return

        if S.__contains__(t):  # t has been handled
            continue

        S.add(t)  # handle t
        G = list(t)  # transform to arr
        k = find(G)  # find 'x' from arr
        t_y, t_x = k // N, k % N  # get positions of 2d arr
        for i in range(4):
            y, x = (t_y + dy[i]), t_x + dx[i]  # get new positions of 2d arr
            v = y * N + x  # new position
            if 0 <= y < N and 0 <= x < N:
                # swap
                G[k], G[v] = G[v], G[k]
                # transform arr to str
                s = ''.join(G)
                if M.__contains__(s) is not True:  # push into queue and change distance
                    Q.push(s)
                    M[s] = M[t] + 1
                # swap to src
                G[k], G[v] = G[v], G[k]
    print(-1)


if __name__ == '__main__':
    bfs(input().replace(' ', ''))
