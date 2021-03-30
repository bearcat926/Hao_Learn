"""
最大异或对
在给定的 N 个整数 A1，A2……AN 中选出两个进行 xor（异或）运算，得到的结果最大是多少？

输入格式
第一行输入一个整数 N。

第二行输入 N 个整数 A1～AN。

输出格式
输出一个整数表示答案。

数据范围
1≤N≤10^5,
0≤Ai<2^31
输入样例：
3
1 2 3
输出样例：
3

01 ^ 10 = 11 = 3
01 ^ 11 = 10 = 2
10 ^ 11 = 01 = 1

2^0 = 1  1   1
2^1 = 2  10  2
2^2 = 4  100 3
  31         32


"""
N = 10 ** 5
A = 31

NODE = [[0] * 2 for i in range(A * N)]
index = 0  # 下标是0的点，既是根节点，又是空节点


def insert(n):
    global index
    global A
    node_num = 0
    for i in range(A - 1, -1, -1):
        c_num = n >> i & 1  # 计算最末尾是0 还是 1
        if NODE[node_num][c_num] == 0:
            index += 1
            NODE[node_num][c_num] = index
        node_num = NODE[node_num][c_num]


def query(n):
    node_num, res = 0, 0
    for i in range(A - 1, -1, -1):
        c_num = n >> i & 1
        rel_num = 1 - c_num  # 二进制取反
        if NODE[node_num][rel_num] > 0:  # 如果对位有值
            node_num = NODE[node_num][rel_num]
            res += 1 << i  # 因为是对位关系，异或得1，再移动响应的位数可得相应位置上异或的值
        else:  # 对位无值，则走相同位
            node_num = NODE[node_num][c_num]
    return res  # 当前能找到的，可以产生最大异或对的值


if __name__ == '__main__':
    max_value = -1
    n = int(input())
    # 十进制整数转二进制整数数组 => list(map(int, format(x, 'b').zfill(32)))
    # s = [list(map(int, format(x, 'b').zfill(A))) for x in list(map(int, input().split()))]
    A_list = list(map(int, input().split()))
    for i in range(n):
        insert(A_list[i])
        # 二进制整数数组转十进制整数 => int(''.join(list(map(str, l))), 2)
        max_value = max(max_value, query(A_list[i]))

    print(max_value)
