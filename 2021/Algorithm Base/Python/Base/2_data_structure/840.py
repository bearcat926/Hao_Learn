"""
模拟散列表
维护一个集合，支持如下几种操作：

“I x”，插入一个数x；
“Q x”，询问数x是否在集合中出现过；
现在要进行N次操作，对于每个询问操作输出对应的结果。

输入格式
第一行包含整数N，表示操作数量。

接下来N行，每行包含一个操作指令，操作指令为”I x”，”Q x”中的一种。

输出格式
对于每个询问指令“Q x”，输出一个询问结果，如果x在集合中出现过，则输出“Yes”，否则输出“No”。

每个结果占一行。

数据范围
1≤N≤10^5
−109≤x≤109
输入样例：
5
I 1
I 2
I 3
Q 2
Q 5
输出样例：
Yes
No

哈希表

    存储结构

        开放寻址法

            只有一个数组，但大小应为限制的两到三倍，且初始值一般是一个特殊标志

        拉链法

            1. 使用 T[x mod r] 存储数据 => r > 10 ^ 5 且 r 应该是一个质数
            2. 解决哈希冲突 => 数组 + 链表

    字符串哈希方式


"""

# def get_N():  # 求质数
#     i = 200000
#     while True:
#         flag = True
#         j = 2
#         while j * j <= i:  #
#             if i % j == 0:
#                 flag = False
#                 break
#             j += 1
#         if flag:  # 找不到可以整数的数，则是质数
#             break
#         i += 1
#     print(i)
#
#
# get_N()

# 拉链法
N = 100003
H, E, NE = [-1] * N, [-1] * N, [-1] * N
index = 0


def insert(x):
    global index
    k = (x % N + N) % N
    E[index] = x
    NE[index] = H[k]
    H[k] = index
    index += 1


def find(x):
    k = (x % N + N) % N
    idx = H[k]
    while idx != -1:
        if x == E[idx]:
            return True
        idx = NE[idx]
    return False


# 开放寻址法（规定长度的两到三倍）
N = 200003
H = [None] * N


def find(x):
    index = (x % N + N) % N
    while H[index] is not None and H[index] != x:
        index += 1
        if index == N:
            index = 0
    return index


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        op, x = map(str, input().split())
        x = int(x)
        if op == 'I':
            H[find(x)] = x
        else:
            print('Yes' if H[find(x)] is not None else 'No')
