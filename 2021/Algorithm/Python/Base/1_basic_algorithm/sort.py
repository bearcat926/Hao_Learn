import random
from math import floor

n = 100
N = [floor(random.random() * n) for i in range(n)]


# 冒泡排序：从无序区选择最大的值插入到有序区的头部, 途中会不断交换数字（把大的放后面）
def bubble_sort():
    i, j = 0, n
    while i < j:
        while i < j - 1:
            if N[i] > N[i + 1]:
                N[i], N[i + 1] = N[i + 1], N[i]
            i += 1
        i = 0
        j -= 1
    print(N)


# 选择排序：从无序区选择最小的值插入到有序区的末尾
def select_sort():
    mix_index = i = j = 0
    for i in range(n):
        while j < n:
            if N[j] < N[mix_index]:
                mix_index = j
            j += 1
        N[i], N[mix_index] = N[mix_index], N[i]
        j = i + 1
    print(N)


"""
插入排序
    [0,j] - 有序区 ; [i,n] - 无序区
    选择无序区的第一个值插入有序区的末尾，之后调整有序区的顺序，使有序区从小到大排列
"""


def insert_sort():
    for i in range(1, n):  # 用 i区分有序无序区域，用 j进行插入操作
        key = N[i]  # 从无序区放入有序区末尾
        j = i - 1  # N[j]表示当前需要与新增值key进行比较的值
        while j >= 0 and N[j] > key:
            N[j], N[j + 1] = N[j + 1], N[j]
            j -= 1  # 当交换完成且j-=1后，新的 N[j]就是仍然是 N[j]表示当前需要与新增值key进行比较的值
    print(N)


# 快速排序
def quick_sort(start, end):
    if start >= end:  # 当前递归只有一个元素，或无元素时退出
        return

    # 为了方便使用do...while进行判断
    i, j = start - 1, end + 1
    # 以 j为基准进行二分
    p = N[(start + end) >> 1]

    while i < j:
        # do ... while 查找不符合排序条件的数
        i += 1
        while N[i] < p:
            i += 1

        j -= 1
        while N[j] > p:
            j -= 1

        if i < j:  # 交换
            N[j], N[i] = N[i], N[j]

    quick_sort(start, j)
    quick_sort(j + 1, end)


# 堆排序
def down(i):  # 调整子树，使父节点变成子树节点中最小的点
    x = i
    if 2 * i < n and N[x] > N[2 * i]:
        x = 2 * i
    if 2 * i + 1 < n and N[x] > N[2 * i + 1]:
        x = 2 * i + 1
    if x != i:
        N[i], N[x] = N[x], N[i]
        down(x)


def heap_sort():
    for i in range(n // 2, -1, -1):  # O(log_n)初始化堆
        down(i)
    size = n
    for i in range(n):
        print(N[1], end=' ')
        # 删除堆顶节点
        N[1] = N[size - 1]
        size -= 1
        down(1)


# 归并排序
def merge_sort(start, end):
    if start >= end:
        return

    # 二分部分
    mid = (start + end) >> 1
    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    # 双指针
    T = []
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if N[i] <= N[j]:
            T.append(N[i])
            i += 1
        else:
            T.append(N[j])
            j += 1

    # 数组余位处理
    while i <= mid:
        T.append(N[i])
        i += 1

    while j <= end:
        T.append(N[j])
        j += 1

    # 复制到原数组
    i, j = start, 0
    while i <= end:
        N[i] = T[j]
        i += 1
        j += 1


"""
计数排序 - 适用于[0, n]的正整数数组排序
"""


def count_sort():
    ms = n
    T = [0] * (ms + 1)
    # 计数
    for i in range(n):
        T[N[i]] += 1
    # 按序输出
    for i in range(0, ms + 1):
        if T[i] != 0:
            while T[i] != 0:
                print(i, end=' ')
                T[i] -= 1


"""
希尔排序 - 缩小增量排序

以gap为增量，调整间隔为增量的一对数字，使其按序排列
随后缩小增量直至为0，即全序列排列成功
"""


def shell_sort():
    gap = n >> 1  # size >> 1
    while gap > 0:  # 当前增量，即对应元素间隔
        i = gap  # i = 0 + gap, 即从 0开始进行增量排序
        while i < n:
            j = i  # j, j-gap 为一对
            while j - gap >= 0 and N[j - gap] > N[j]:  # j-gap>=0 为退出条件
                N[j - gap], N[j] = N[j], N[j - gap]
                j -= gap  # 交换完成，退出循环 => break
            i += 1  # 比较下一对
        gap = gap >> 1  # 缩小增量
    print(N)


"""
基数排序

"""


def get_digital(i, d, l):  # 获取对应位置的值
    if d <= l:
        i //= 10 ** (d - 1)
        return i % 10
    return 0


def radix_sort():  # 常规的二维数组做法
    r, l = 1, len(str(n))  # 当前位及位数限制
    B = [([0] * (n + 1)) for x in range(10)]  # 桶
    C = [0] * 10  # 计数
    while r <= l:  # 循环所有位
        for i in range(len(N)):  # 将元素按当前位的值放入对应的桶
            d = get_digital(N[i], r, l)
            B[d][C[d]] = N[i]
            C[d] += 1
        j = 0
        for i in range(10):  # 根据桶下标顺序排序
            k = 0
            while k < C[i]:
                N[j] = B[i][k]
                j += 1
                k += 1
            C[i] = 0
        r += 1
    print(N)


def radix_sort2():  # 一维数组桶进行空间优化
    global N
    r, l = 1, len(str(n))  # 当前位及位数限制
    B = [0] * n  # 桶
    C = [0] * (10 + 1)  # 计数，空出第0位，用i位计数某位数为i-1的数，可以避免反序的情况
    while r <= l:  # 循环所有位
        for i in range(len(N)):  # 计算当前位桶中的元素数量（空出数组第0位）
            d = get_digital(N[i], r, l)
            C[d + 1] += 1
        for i in range(1, 10 + 1):  # 计算桶的范围 => 第 d位桶中元素在 B数组中的下标范围 [ C[d] ~ C[d+1]-1 ]
            C[i] += C[i - 1]
        for i in range(len(N)):  # 将元素放置到对应桶中
            d = get_digital(N[i], r, l)
            B[C[d]] = N[i]  # C[d] 表示 第d位桶中的当前元素索引
            C[d] += 1  # 索引 +1
        for i in range(len(N)):  # 复制到原数组
            N[i] = B[i]
        r += 1
        C = [0] * (10 + 1)  # 刷新计数数组
    print(N)


if __name__ == '__main__':
    # bubble_sort()
    # select_sort()
    # insert_sort()
    # quick_sort(0, n - 1), print(N)
    # heap_sort()
    # merge_sort(0, n - 1), print(N)
    # count_sort()
    # shell_sort()
    # radix_sort()
    radix_sort2()