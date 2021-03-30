"""
快速排序
给定你一个长度为n的整数数列。

请你使用快速排序对这个数列按照从小到大进行排序。

并将排好序的数列按顺序输出。

输入格式
输入共两行，第一行包含整数 n。

第二行包含 n 个整数（所有整数均在1~109范围内），表示整个数列。

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
import random
from math import floor


def quicksort(nums, start, end):
    if start >= end:
        return

    pivot = nums[(start + end) >> 1]  # 轴值
    left, right = start - 1, end + 1

    while left < right:
        """
            由于使用do-while循环, 所以i和j一定会自增, 使得循环会继续下去
            但是如果采用while循环(i和j的初始化做出对应的变更), 
            i和j在特殊情况下（当nums[left]和nums[right]都为 pivot 时）不自增的话, 
            循环就会卡死
        """
        left += 1  # do...while...
        while nums[left] < pivot:
            left += 1

        right -= 1
        while nums[right] > pivot:
            right -= 1

        if left < right:  # swap
            nums[left], nums[right] = nums[right], nums[left]

    quicksort(nums, start, right)
    quicksort(nums, right + 1, end)


if __name__ == '__main__':
    # length = int(input())
    # nums = [int(x) for x in input().split()]
    length = 100
    nums = [floor(random.random() * length) for i in range(length)]
    quicksort(nums, 0, length - 1)
    for i in nums:
        print(i, end=' ')

# 三路快排
# def quick_sort(nums):
#     if (len(nums) <= 1): return nums;
#
#     privot = nums[len(nums) // 2]
#     left = [x for x in nums if x < privot]
#     mid = [x for x in nums if x == privot]
#     right = [x for x in nums if x > privot]
#     # print (" ".join(list(map(str, left))) +","+ str(mid[0]) +","+" ".join(list(map(str, right))) )
#     return quick_sort(left) + mid + quick_sort(right)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     nums = list(map(int, input().split()))
#     nums = quick_sort(nums)
#     print(" ".join(list(map(str, nums))))
