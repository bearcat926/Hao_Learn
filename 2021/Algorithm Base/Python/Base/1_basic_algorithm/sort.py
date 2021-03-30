import random
from math import floor

n = 100
N = [floor(random.random() * n) for i in range(n)]


# 冒泡排序
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


# 选择排序
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


# 插入排序
def insert_sort():
    for i in range(1, n):
        key = N[i]
        j = i - 1
        while j >= 0 and N[j] > key:
            N[j], N[j + 1] = N[j + 1], N[j]
            j -= 1

    print(N)


# 快速排序
def quick_sort(start, end):
    if start >= end:
        return

    p = N[(start + end) >> 1]
    i, j = start - 1, end + 1

    while i < j:
        i += 1
        while N[i] < p:
            i += 1

        j -= 1
        while N[j] > p:
            j -= 1

        if i < j:
            N[j], N[i] = N[i], N[j]

    quick_sort(start, j)
    quick_sort(j + 1, end)


# 堆排序
def down(i):
    x = i
    if 2 * i < n and N[x] > N[2 * i]:
        x = 2 * i
    if 2 * i + 1 < n and N[x] > N[2 * i + 1]:
        x = 2 * i + 1
    if x != i:
        N[i], N[x] = N[x], N[i]
        down(x)


def heap_sort():
    for i in range(n // 2, -1, -1):  # init
        down(i)
    size = n
    for i in range(n):
        print(N[1], end=' ')
        N[1] = N[size - 1]
        size -= 1
        down(1)


# 归并排序
def merge_sort(start, end):
    if start >= end:
        return

    p = (start + end) >> 1
    merge_sort(start, p)
    merge_sort(p + 1, end)

    T = []
    i, j = start, p + 1
    while i <= p and j <= end:
        if N[i] <= N[j]:
            T.append(N[i])
            i += 1
        else:
            T.append(N[j])
            j += 1

    while i <= p:
        T.append(N[i])
        i += 1

    while j <= end:
        T.append(N[j])
        j += 1

    i, j = start, 0
    while i <= end:
        N[i] = T[j]
        i += 1
        j += 1


# 计数排序(0 - n)
def count_sort():
    ms = n
    T = [0] * (ms + 1)
    for i in range(n):
        T[N[i]] += 1
    for i in range(0, ms + 1):
        if T[i] != 0:
            while T[i] != 0:
                print(i, end=' ')
                T[i] -= 1


# 希尔排序 - 缩小增量排序
def shell_sort():
    gap = n >> 1  # size >> 1
    while gap > 0:
        i = gap
        while i < n:
            j = i
            while j - gap >= 0 and N[j - gap] > N[j]:
                N[j - gap], N[j] = N[j], N[j - gap]
                j -= gap  # 交换完成，退出循环 => break
            i += 1
        gap = gap >> 1
    print(N)


# 基数排序
def get_digital(i, d, l):  # 获取对应位置的值
    if d <= l:
        i //= 10 ** (d - 1)
        return i % 10

    return 0


def radix_sort():  # 常规的二维数组做法
    r, l = 1, len(str(n))
    B = [([0] * (n + 1)) for x in range(10)]
    C = [0] * 10

    while r <= l:
        for i in N:
            d = get_digital(i, r, l)
            B[d][C[d]] = i
            C[d] += 1
        j = 0
        for i in range(10):
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
    r, l = 1, len(str(n))
    B = [0] * (n + 1)
    C = [0] * (10 + 1)  # 空出第0位，用i位计数某位数为i-1的数，可以避免反序的情况
    while r <= l:
        for i in N:  # 分桶计数
            d = get_digital(i, r, l)
            C[d + 1] += 1
        for i in range(1, 10 + 1):  # 计算桶的坐标区域
            C[i] += C[i - 1]
        for i in N:  # 分桶
            d = get_digital(i, r, l)
            B[C[d]] = i  # C[d] 表示 某位数为d的桶的开始坐标
            C[d] += 1
        C = [0] * (10 + 1)  # 刷新计数数组
        for i in range(len(N)):
            N[i] = B[i]
        r += 1
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