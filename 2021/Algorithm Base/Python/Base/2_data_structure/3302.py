"""
表达式求值
给定一个表达式，其中运算符仅包含 +,-,*,/（加 减 乘 整除），可能包含括号，请你求出表达式的最终值。

注意：

数据保证给定的表达式合法。
题目保证符号 - 只作为减号出现，不会作为负号出现，例如，-1+2,(2+2)*(-(1+1)+2) 之类表达式均不会出现。
题目保证表达式中所有数字均为正整数。
题目保证表达式在中间计算过程以及结果中，均不超过 231−1。
题目中的整除是指向 0 取整，也就是说对于大于 0 的结果向下取整，例如 5/3=1，对于小于 0 的结果向上取整，例如 5/(1−4)=−1。
C++和Java中的整除默认是向零取整；Python中的整除//默认向下取整，因此Python的eval()函数中的整除也是向下取整，在本题中不能直接使用。
输入格式
共一行，为给定表达式。

输出格式
共一行，为表达式的结果。

数据范围
表达式的长度不超过 10^5。

输入样例：
(2+2)*(1+1)
输出样例：
8

python 取整方式

    向上取整：math.ceil()
    向下取整：math.floor()、整除"//"
    四舍五入：round() —— 奇数向远离0取整，偶数去尾取整；或言之：奇数进位，偶数去尾
    向0取整：int()

后缀表达式

                                 x
                               /  \
       (2 + 2) x (1 + 1) =>   +    +   =>  2 2 + 1 1 + x
                            /  \  / \
                           2   2 1   1
"""
import math
import re


class stack:
    def __init__(self, size):
        self.D = [0] * (size + 10)
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


N = 10 ** 5
NUM = stack(N)
OP = stack(N)
pr = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
reg = re.compile('^[0-9]*$')


def calc():
    b = NUM.pop()
    a = NUM.pop()
    op = OP.pop()
    x = 0
    if op == '+':
        x = a + b
    elif op == '-':
        x = a - b
    elif op == '*':
        x = a * b
    else:
        x = a / b
    NUM.push(int(x))


if __name__ == '__main__':
    s = list(map(str, input()))
    i = 0
    while i < len(s):  # is digital
        c = s[i]
        if reg.match(c):
            c = int(c)
            while i + 1 < len(s) and reg.match(s[i + 1]):
                i += 1
                c = c * 10 + int(s[i])
            NUM.push(c)
        elif c == '(':
            OP.push(c)
        elif c == ')':
            while OP.query() != '(':
                calc()
            OP.pop()
        else:  # calculation
            while not OP.empty() and pr[OP.query()] >= pr[c]:  # 操作符栈中不为空，且符号优先级大于当前优先级则优先计算再入栈
                calc()
            OP.push(c)
        i += 1
    while not OP.empty():
        calc()
    print(NUM.pop())
