"""
逆序对的数量
给定一个长度为n的整数数列，请你计算数列中的逆序对的数量。

逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i < j 且 a[i] > a[j]，则其为一个逆序对；否则不是。

输入格式
第一行包含整数n，表示数列的长度。

第二行包含 n 个整数，表示整个数列。

输出格式
输出一个整数，表示逆序对的个数。

数据范围
1 ≤ n ≤ 100000
输入样例：
6
2 3 4 5 6 1
输出样例：
5
"""


def merge_sort(nums):
    if len(nums) <= 1:
        return 0
    mid = len(nums) // 2
    L = nums[:mid]
    R = nums[mid:]
    ans = merge_sort(L) + merge_sort(R)

    # 归并的过程
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
            ans += len(L) - i  # 当且仅当L[i] > R[j]时，才存在逆序对
        k += 1                 # 且由于子数组单调递增， 则L[i]及其之后元素都可以与R[j]组成逆序对，则会产生len(L) - i个逆序对

    while i < len(L):
        nums[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        nums[k] = R[j]
        k += 1
        j += 1

    return ans


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(merge_sort(nums))
