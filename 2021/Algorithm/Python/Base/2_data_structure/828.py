"""
模拟栈
实现一个栈，栈初始为空，支持四种操作：

(1) “push x” – 向栈顶插入一个数x；

(2) “pop” – 从栈顶弹出一个数；

(3) “empty” – 判断栈是否为空；

(4) “query” – 查询栈顶元素。

现在要对栈进行M个操作，其中的每个操作3和操作4都要输出相应的结果。

输入格式
第一行包含整数M，表示操作次数。

接下来M行，每行包含一个操作命令，操作命令为”push x”，”pop”，”empty”，”query”中的一种。

输出格式
对于每个”empty”和”query”操作都要输出一个查询结果，每个结果占一行。

其中，”empty”操作的查询结果为“YES”或“NO”，”query”操作的查询结果为一个整数，表示栈顶元素的值。

数据范围
1 ≤ M ≤ 100000,
1 ≤ x ≤ 10^9
所有操作保证合法。

输入样例：
10
push 5
query
push 6
pop
query
pop
empty
push 4
query
empty
输出样例：
5
5
YES
4
NO
"""
N = 100000


class stack:
    def __init__(self):
        self.D = [0] * (N + 10)
        self.top = -1  # 直接取

    def empty(self):
        return self.top == -1

    def push(self, e):
        if self.top < len(self.D):
            self.top += 1
            self.D[self.top] = e

    def pop(self):
        if not self.empty():
            self.top -= 1
            return self.D[self.top + 1]

    def query(self):
        if not self.empty():
            return self.D[self.top]


if __name__ == '__main__':
    s = stack()
    m = int(input())
    while m != 0:
        m -= 1
        op, *p = input().split()
        if op == 'pop':
            s.pop()
        elif op == 'empty':
            print('YES' if s.empty() else 'NO')
        elif op == 'push':
            s.push(int(p[0]))
        elif op == 'query':
            print(s.query())