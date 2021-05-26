"""
归并排序
给定你一个长度为n的整数数列。

请你使用归并排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

输入格式
输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在1~10^9范围内），表示整个数列。

输出格式
输出共一行，包含 n 个整数，表示排好序的数列。

数据范围
1 ≤ n ≤ 100000
输入样例：
5
3 1 2 4 5
输出样例：
1 2 3 4 5
"""
n = int(input())
list1 = list(map(int, input().split()))


def merge_sort(list):
    if len(list) <= 1:
        return
    mid = len(list) // 2  # 确定分界点
    L = list[:mid]
    R = list[mid:]
    merge_sort(L)  # 递归排左边
    merge_sort(R)  # 右边

    # 双指针算法
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    merge_sort(list1)
    for i in list1:
        print(i, end=" ")
