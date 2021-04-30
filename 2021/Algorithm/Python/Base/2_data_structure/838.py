"""
堆排序
输入一个长度为n的整数数列，从小到大输出前m小的数。

输入格式
第一行包含整数n和m。

第二行包含n个整数，表示整数数列。

输出格式
共一行，包含m个整数，表示整数数列中前m小的数。

数据范围
1≤m≤n≤10^5，
1≤数列中元素≤109
输入样例：
5 3
4 5 1 3 2
输出样例：
1 2 3


如何手写一个堆？

    1. 插入一个数            size += 1; head[size] = x; up(size)
    2. 求集合中的最小值       head[1]
    3. 删除最小值            head[1] = head[size]; size -= 1; down(1)
    4. 删除任意一个元素       head[k] = head[size]; size -= 1; down(k); up(k) -> 只会执行一个
    5. 修改任意一个元素       head[k] = x; down(k); up(k) -> 只会执行一个

堆的基本结构 - 二叉树

    父节点小于（或大于）左右孩子 -> 需要看最大堆还是最小堆

存储

    根节点为 1, 左孩子为2x, 右孩子为2x+1

基本操作

    down: 往下调整
    up  : 往上调整

"""
N = 10 ** 5
HEAP = [0]
size = 0


def down(i):
    global HEAP
    global size
    x = i
    # 父节点比左孩子大
    if i * 2 <= size and HEAP[i * 2] < HEAP[x]:
        x = i * 2
    # 当前节点比右孩子大
    if i * 2 + 1 <= size and HEAP[i * 2 + 1] < HEAP[x]:
        x = i * 2 + 1
    if x != i:  # 值有变化了, 当前x是三个值中最小的
        # 进行交换
        HEAP[x], HEAP[i] = HEAP[i], HEAP[x]
        down(x)


def init(list):
    global HEAP
    global size
    HEAP += list
    size = len(list)
    # S = n/4 * 1 + n/8 * 2 + n/16 * 3 + ... + n/2^n * (n-1) < n
    # n/4 * 1 => 堆中的倒数第2层节点down时，移动1次
    for i in range(size // 2, -1, -1):
        down(i)


def remove(i):
    global HEAP
    global size
    HEAP[i] = HEAP[size]
    size -= 1
    down(i)
    # up(i)


def dump_sort():
    print(HEAP[1], end=' ')
    remove(1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    D = list(map(int, input().split()))

    init(D)
    for i in range(m):
        dump_sort()
