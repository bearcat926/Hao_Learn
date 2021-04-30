"""
字符串哈希
给定一个长度为n的字符串，再给定m个询问，每个询问包含四个整数l1,r1,l2,r2，请你判断[l1,r1]和[l2,r2]这两个区间所包含的字符串子串是否完全相同。

字符串中只包含大小写英文字母和数字。

输入格式
第一行包含整数n和m，表示字符串长度和询问次数。

第二行包含一个长度为n的字符串，字符串中只包含大小写英文字母和数字。

接下来m行，每行包含四个整数l1,r1,l2,r2，表示一次询问所涉及的两个区间。

注意，字符串的位置从1开始编号。

输出格式
对于每个询问输出一个结果，如果两个字符串子串完全相同则输出“Yes”，否则输出“No”。

每个结果占一行。

数据范围
1≤n,m≤10^5
输入样例：
8 3
aabbaabb
1 3 5 7
1 3 6 8
1 2 1 2
输出样例：
Yes
No
Yes


哈希表

    存储结构

        开放寻址法

            只有一个数组，但大小应为限制的两到三倍，且初始值一般是一个特殊标志

        拉链法

            1. 使用 T[x mod r] 存储数据 => r > 10 ^ 5 且 r 应该是一个质数
            2. 解决哈希冲突 => 数组 + 链表

    字符串哈希方式

        字符串前缀哈希法

            举例

                若 str = 'ABCDEFG'
                h[0] = 0
                h[1] = hash('A')
                h[2] = hash('AB')
                h[3] = hash('ABC')
                h[4] = hash('ABCD')
                ......

                假设 'ABCD' = (1234)p -> ABCD为  P进制下的1234
                则hash = (1 * P^3 + 2 * P^2 + 3 * P^1 + 4 * P^0) mod Q

                注意：
                    1. 不能映射成 0
                    2. 设不会发生hash碰撞
                        取值经验：
                        当P = 131 or 13331时，Q = 2^64

            求值过程

                                      |---hash---|
                         |-----------^L---------R---------|
            index        1          L-1         R
            hash[R]     R-1                     0
            hash[L-1]   L-2         0
                已知知道hash[R]和 hash[L-1],求 hash[L~R]。

                从 L - 1移动到 L 需要走 1 位，
                设 L = 1, 则 L + (R - L) = R - L + 1

                求hash公式(先对齐在减):
                   H[R] - H[L-1] * P ^ (R - L + 1)

                当 Q = 2^64时，使用long类型存储 代替 mod Q 操作

                |-----------^L---------R---------|

"""
from numpy import long  # python2 中可以使用，但在 python3 中删除，在python3中的整数都为int

N = 10 ** 5
H = [0] * (N + 1)  # MLE优化1
P = [0] * (N + 1)
NUM_P = 131
NUM_Q = 256 ** 8  # 2 ** 64 => 2 ** (8 * 8)


# 计算区间内的hash值
def get(L, R):
    return (H[R] - H[L - 1] * P[R - L + 1]) % NUM_Q


if __name__ == '__main__':
    n, m = map(int, input().split())
    S = [''] + list(input())
    P[0] = 1
    for i in range(1, n + 1):
        # 计算 P的乘方值
        P[i] = (P[i - 1] * NUM_P) % NUM_Q  # MLE优化2
        # 计算哈希值 (1 * P^3 + 2 * P^2 + 3 * P^1 + 4 * P^0) mod Q
        # H[i - 1] * NUM_P 是进位
        H[i] = (H[i - 1] * NUM_P + ord(S[i])) % NUM_Q

    for i in range(m):
        l1, r1, l2, r2 = map(int, input().split())
        # 两个字符串子串完全相同
        print('Yes' if get(l1, r1) == get(l2, r2) else 'No')
