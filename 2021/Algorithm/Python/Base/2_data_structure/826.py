"""
单链表
实现一个单链表，链表初始为空，支持三种操作：

(1) 向链表头插入一个数；

(2) 删除第k个插入的数后面的数；

(3) 在第k个插入的数后插入一个数

现在要对该链表进行M次操作，进行完所有操作后，从头到尾输出整个链表。

注意:题目中第k个插入的数并不是指当前链表的第k个数。例如操作过程中一共插入了n个数，则按照插入的时间顺序，这n个数依次为：第1个插入的数，第2个插入的数，…第n个插入的数。

输入格式
第一行包含整数M，表示操作次数。

接下来M行，每行包含一个操作命令，操作命令可能为以下几种：

(1) “H x”，表示向链表头插入一个数x。

(2) “D k”，表示删除第k个插入的数后面的数（当k为0时，表示删除头结点）。

(3) “I k x”，表示在第k个插入的数后面插入一个数x（此操作中k均大于0）。

输出格式
共一行，将整个链表从头到尾输出。

数据范围
1≤M≤100000
所有操作保证合法。

输入样例：
10
H 9
I 1 1
D 1
D 0
H 6
I 3 6
I 4 5
I 4 5
I 3 4
D 6
输出样例：
6 4 6 5
"""
N = 100000


class single_linked_list:
    def __init__(self):
        self.index = 0
        self.head = -1
        self.D, self.NE = [-1] * (N + 10), [-1] * (N + 10)

    def insert(self, e):  # 向链表头插入一个数
        self.D[self.index] = e
        self.NE[self.index] = self.head
        self.head = self.index
        self.index += 1

    # D的存放顺序就是插入顺序, D[0]是第1个插入的值
    def insert_k(self, k, e):  # 在第k个[k - 1]插入的数后插入一个数
        self.D[self.index] = e
        self.NE[self.index] = self.NE[k - 1]
        self.NE[k - 1] = self.index
        self.index += 1

    def delete(self, k):  # 删除第k个插入的数后面的数
        if k == 0:
            self.head = self.NE[self.head]
        else:
            self.NE[k - 1] = self.NE[self.NE[k - 1]]

    def print(self):
        i = self.head
        print(self.D[i], end=' ')
        while self.NE[i] != -1:
            i = self.NE[i]
            print(self.D[i], end=' ')


if __name__ == '__main__':
    l = single_linked_list()
    m = int(input())
    while m != 0:
        m -= 1
        s, *p = input().split()
        op = str(s)
        if op == 'H':
            l.insert(int(p[0]))
        elif op == 'D':
            l.delete(int(p[0]))
        elif op == 'I':
            k, e = map(int, p)
            l.insert_k(k, e)
    l.print()
