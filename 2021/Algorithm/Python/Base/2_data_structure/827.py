"""
双链表
实现一个双链表，双链表初始为空，支持5种操作：

(1) 在最左侧插入一个数；

(2) 在最右侧插入一个数；

(3) 将第k个插入的数删除；

(4) 在第k个插入的数左侧插入一个数；

(5) 在第k个插入的数右侧插入一个数

现在要对该链表进行M次操作，进行完所有操作后，从左到右输出整个链表。

注意:题目中第k个插入的数并不是指当前链表的第k个数。例如操作过程中一共插入了n个数，则按照插入的时间顺序，这n个数依次为：第1个插入的数，第2个插入的数，…第n个插入的数。

输入格式
第一行包含整数M，表示操作次数。

接下来M行，每行包含一个操作命令，操作命令可能为以下几种：

(1) “L x”，表示在链表的最左端插入数x。

(2) “R x”，表示在链表的最右端插入数x。

(3) “D k”，表示将第k个插入的数删除。

(4) “IL k x”，表示在第k个插入的数左侧插入一个数。

(5) “IR k x”，表示在第k个插入的数右侧插入一个数。

输出格式
共一行，将整个链表从左到右输出。

数据范围
1 ≤ M ≤ 100000
所有操作保证合法。

输入样例：
10
R 7
D 1
L 3
IL 2 10
D 3
IL 2 7
L 8
R 9
IL 4 7
IR 2 2
输出样例：
8 7 7 3 2 9
"""
N = 100000


class double_linked_list:
    def __init__(self):
        self.left = 0
        self.right = 1
        self.index = 2
        self.D, self.L, self.R = [0] * (N + 10), [0] * (N + 10), [0] * (N + 10)
        self.R[self.left], self.L[self.right] = self.right, self.left

    def insert_left(self, e):  # 向左链表头插入一个数
        # 插入
        self.D[self.index] = e
        self.R[self.index] = self.R[self.left]
        self.L[self.index] = self.left
        # 最左节点的左指针
        self.L[self.R[self.left]] = self.index
        # 左指针
        self.R[self.left] = self.index
        self.index += 1

    def insert_right(self, e):  # 向链表头插入一个数
        # 插入
        self.D[self.index] = e
        self.L[self.index] = self.L[self.right]
        self.R[self.index] = self.right
        # 最右节点的右指针
        self.R[self.L[self.right]] = self.index
        # 右指针
        self.L[self.right] = self.index
        self.index += 1

    # D的存放顺序就是插入顺序, D[2]是第1个插入的值
    def insert_left_k(self, k, e):  # 在第k[k + 1]个插入的数左侧插入一个数
        self.D[self.index] = e
        # 处理插入数的左侧关系
        self.R[self.index] = k + 1
        self.L[self.index] = self.L[k + 1]
        # 处理插入数的右侧关系
        self.R[self.L[k + 1]] = self.index
        self.L[k + 1] = self.index
        self.index += 1

    # D的存放顺序就是插入顺序, D[0]是第1个插入的值
    def insert_right_k(self, k, e):  # 在第k个插入的数右侧插入一个数
        self.D[self.index] = e
        # 处理插入数的右侧关系
        self.L[self.index] = k + 1
        self.R[self.index] = self.R[k + 1]
        # 处理插入数的左侧关系
        self.L[self.R[k + 1]] = self.index
        self.R[k + 1] = self.index
        self.index += 1

    def delete(self, k):  # 将第k个插入的数删除
        self.L[self.R[k + 1]] = self.L[k + 1]
        self.R[self.L[k + 1]] = self.R[k + 1]

    def print(self):
        i = self.R[self.left]
        while self.R[i] != self.right:
            print(self.D[i], end=' ')
            i = self.R[i]
        print(self.D[i], end=' ')


if __name__ == '__main__':
    l = double_linked_list()
    m = int(input())
    while m != 0:
        m -= 1
        s, *p = input().split()
        op = str(s)
        if op == 'L':
            l.insert_left(int(p[0]))
        elif op == 'R':
            l.insert_right(int(p[0]))
        elif op == 'D':
            l.delete(int(p[0]))
        elif op == 'IL':
            k, e = map(int, p)
            l.insert_left_k(k, e)
        elif op == 'IR':
            k, e = map(int, p)
            l.insert_right_k(k, e)
    l.print()