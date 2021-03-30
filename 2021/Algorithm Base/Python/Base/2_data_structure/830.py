"""
单调栈
给定一个长度为N的整数数列，输出每个数左边第一个比它小的数，如果不存在则输出-1。

输入格式
第一行包含整数N，表示数列长度。

第二行包含N个整数，表示整数数列。

输出格式
共一行，包含N个整数，其中第i个数表示第i个数的左边第一个比它小的数，如果不存在则输出-1。

数据范围
1≤N≤10^5
1≤数列中元素≤10^9
输入样例：
5
3 4 2 7 5
输出样例：
-1 3 -1 2 2

"""
N = 100000
head = -1
STK = [0] * (N + 10)

if __name__ == '__main__':
    n = int(input())
    P = list(map(int, input().split()))
    for i in range(n):
        while head >= 0 and STK[head] >= P[i]:  # 果栈顶元素大于等于（单调）当前待入栈元素，则出栈
            head -= 1
        print('-1' if head == -1 else STK[head], end=' ')  # 打印当前值
        head += 1  # 存新值
        STK[head] = P[i]