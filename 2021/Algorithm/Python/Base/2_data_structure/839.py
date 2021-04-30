"""
模拟堆
维护一个集合，初始时集合为空，支持如下几种操作：

“I x”，插入一个数x；
“PM”，输出当前集合中的最小值；
“DM”，删除当前集合中的最小值（数据保证此时的最小值唯一）；
“D k”，删除第k个插入的数；
“C k x”，修改第k个插入的数，将其变为x；
现在要进行N次操作，对于所有第2个操作，输出当前集合的最小值。

输入格式
第一行包含整数N。

接下来N行，每行包含一个操作指令，操作指令为”I x”，”PM”，”DM”，”D k”或”C k x”中的一种。

输出格式
对于每个输出指令“PM”，输出一个结果，表示当前集合中的最小值。

每个结果占一行。

数据范围
1≤N≤10^5
−109≤x≤109
数据保证合法。

输入样例：
8
I -10
PM
I -10
D 1
C 2 8
I 6
PM
DM
输出样例：
-10
6

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
HEAP = [0] * (N + 10)
PH = [0] * (N + 10)  # PH[k] = i => 第k个插入的值在堆中的下标为i
HP = [0] * (N + 10)  # HP[i] = k => 在堆中的下标为i的节点是第k个插入的值
size, index = 0, 0


def heap_swap(a, b):
    global PH, HEAP, HP
    # 交换插入值的索引
    PH[HP[a]], PH[HP[b]] = b, a
    # 交换索引对应的插入值
    HP[a], HP[b] = HP[b], HP[a]
    # 交换值
    HEAP[a], HEAP[b] = HEAP[b], HEAP[a]


def down(i):
    global HEAP, size
    x = i
    # 父节点比左孩子大
    if i * 2 <= size and HEAP[i * 2] < HEAP[x]:
        x = i * 2
    # 当前节点比右孩子大
    if i * 2 + 1 <= size and HEAP[i * 2 + 1] < HEAP[x]:
        x = i * 2 + 1
    if x != i:  # 值有变化了, 当前x是三个值中最小的
        heap_swap(x, i)
        down(x)


def up(i):
    global HEAP
    # if i != 1:  # 边界
    #     # 先确定当前节点现在是左孩子还是右孩子
    #     p_i = (i - 1) // 2 if i & 1 == 1 else i // 2
    #     # 如果是奇数 => 2 * x + 1 所以是右孩子, 否则是左孩子
    #     while i != 1 and HEAP[p_i] > HEAP[i]:  # 孩子比父节点小
    #         heap_swap(p_i, i)
    #         # up(p_i)
    #         # 缩减递归
    #         i = p_i
    #         p_i = (p_i - 1) // 2 if p_i & 1 == 1 else p_i // 2

    # i // 2 => i // 2 > 0
    # i 为奇数时，i // 2 向下取整
    while i // 2 and HEAP[i // 2] > HEAP[i]:  # 跟父节点交换 直到父节点小于等于此节点
        heap_swap(i // 2, i)
        i //= 2


# def init(list):
#     global HEAP, size
#     HEAP += list
#     size = len(list)
#     # S = n/4 * 1 + n/8 * 2 + n/16 * 3 + ... + n/2^n * (n-1) < n
#     # n/4 * 1 => 堆中的倒数第2层节点down时，移动1次
#     for i in range(size // 2, -1, -1):
#         down(i)


def insert(x):
    global HEAP, PH, HP, size, index
    size += 1
    HEAP[size] = x
    # 维护插入顺序
    index += 1
    PH[index] = size
    HP[size] = index
    up(size)


def remove(i):
    global size
    heap_swap(i, size)
    size -= 1
    down(i)
    up(i)


def remove_elem(k):
    global PH
    remove(PH[k])


def modify_elem(k, x):
    global HEAP, PH
    i = PH[k]
    # 赋值
    HEAP[i] = x
    down(i)
    up(i)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        op, *p = map(str, input().split())
        p = list(map(int, p))
        if op == 'I':  # 插入一个数x
            insert(*p)
        elif op == 'PM':  # 输出当前集合中的最小值
            print(HEAP[1])
        elif op == 'DM':  # 删除当前集合中的最小值（数据保证此时的最小值唯一）
            remove(1)
        elif op == 'D':  # 删除第k个插入的数
            remove_elem(*p)
        elif op == 'C':  # 修改第k个插入的数，将其变为x
            modify_elem(*p)
