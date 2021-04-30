"""
Trie字符串统计
维护一个字符串集合，支持两种操作：

“I x”向集合中插入一个字符串x；
“Q x”询问一个字符串在集合中出现了多少次。
共有N个操作，输入的字符串总长度不超过 10^5，字符串仅包含小写英文字母。

输入格式
第一行包含整数N，表示操作数。

接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。

输出格式
对于每个询问指令”Q x”，都要输出一个整数作为结果，表示x在集合中出现的次数。

每个结果占一行。

数据范围
1≤N≤2∗104
输入样例：
5
I abc
Q abc
Q ab
I ab
Q ab
输出样例：
1
0
1


Trie 树： 高效的存储和查找字符串集合的数据结构

假设存储以下字符串：
    abcdef    abdef    aced    bcdf    bcff    cdaa    bcdc    abc

                 root
                   O
                /  \  \
               a   b   c
              / \   \   \
             b   c   c   d
            / \  |   | \   \
          (c)  d e   d  f   a
          /    | \  |  \  \  \
         d     e (d)(f)(c)(f)(a)
        /      |
       e      (f)
      /
    (f)

快速查找：

"""
N = 2 * 10 ** 4
a_num = ord('a')

NODE = [[0] * 26 for i in range(N + 10)]
CNT = [0] * (N + 10)
index = 0  # 下标是0的点，既是根节点，又是空节点


def insert(str):
    global index
    node_num = 0
    for i in range(len(str)):
        c_num = ord(str[i]) - a_num  # 字符映射
        if NODE[node_num][c_num] == 0:  # 该节点未使用
            index += 1  # 新节点的索引 = 当前使用的索引数量 + 1
            NODE[node_num][c_num] = index
        node_num = NODE[node_num][c_num]

    CNT[node_num] += 1  # 该字符串出现次数增加一次


def query(str):
    node_num = 0
    for i in range(len(str)):
        c_num = ord(str[i]) - a_num
        if NODE[node_num][c_num] == 0:  # 该节点未使用
            return 0
        node_num = NODE[node_num][c_num]

    return CNT[node_num]


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        op, s = map(str, input().split())
        if op == 'I':
            insert(s)
        elif op == 'Q':
            print(query(s))
