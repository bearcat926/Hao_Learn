"""
第k个数
给定一个长度为n的整数数列，以及一个整数k，请用快速选择算法求出数列从小到大排序后的第k个数。

输入格式
第一行包含两个整数 n 和 k。

第二行包含 n 个整数（所有整数均在1~10^9范围内），表示整数数列。

输出格式
输出一个整数，表示数列的第k小数。

数据范围
1 ≤ n ≤ 100000,
1 ≤ k ≤ n
输入样例：
5 3
2 4 1 5 3
输出样例：
3
"""


def quick_select(start, end, k):
    if start == end:  # 只有一个数字时返回，该数字为第k小的数
        return nums[start]

    left, right = start - 1, end + 1
    pivot = nums[(start + end) >> 1]

    while left < right:
        left += 1
        while nums[left] < pivot:
            left += 1

        right -= 1
        while nums[right] > pivot:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    # right = left or right < left
    length = right - start + 1  # 左半区间的区间长度
    if k <= length:  # k在左半区
        return quick_select(start, right, k)
    else:  # k在右半区
        return quick_select(right + 1, end, k - length)


if __name__ == '__main__':
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res = quick_select(0, n - 1, k)
    print(res)
