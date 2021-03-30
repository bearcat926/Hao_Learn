"""
数的范围
给定一个按照升序排列的长度为n的整数数组，以及 q 个查询。

对于每个查询，返回一个元素k的起始位置和终止位置（位置从0开始计数）。

如果数组中不存在该元素，则返回“-1 -1”。

输入格式
第一行包含整数n和q，表示数组长度和询问个数。

第二行包含n个整数（均在1~10000范围内），表示完整数组。

接下来q行，每行包含一个整数k，表示一个询问元素。

输出格式
共q行，每行包含两个整数，表示所求元素的起始位置和终止位置。

如果数组中不存在该元素，则返回“-1 -1”。

数据范围
1 ≤ n ≤ 100000
1 ≤ q ≤ 10000
1 ≤ k ≤ 10000
输入样例：
6 3
1 2 2 3 3 4
3
4
5
输出样例：
3 4
5 5
-1 -1
"""


def get_left_bound(nums, x):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= x:
            right = mid
        else:
            left = mid + 1
    if nums[left] != x:
        return -1
    return left


def get_right_bound(nums, x):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right + 1) >> 1
        if nums[mid] <= x:
            left = mid
        else:
            right = mid - 1
    if nums[left] != x:
        return -1
    return left


if __name__ == "__main__":
    [nums_length, query] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    for _ in range(query):
        x = int(input())
        left_bound = get_left_bound(nums, x)
        right_bound = -1
        if left_bound != -1:  # left_bound = -1时，数组中不存在x
            right_bound = get_right_bound(nums, x)
        print("{} {}".format(left_bound, right_bound))

"""
整数二分模板:

版本1
当我们将区间[l, r]划分成[l, mid]和[mid + 1, r]时，
其更新操作是r = mid或者l = mid + 1;，计算mid时不需要加1。

def binary_search_1(l, r):
    while l < r:
        mid = l + r >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l

版本2
当我们将区间[l, r]划分成[l, mid - 1]和[mid, r]时，
其更新操作是r = mid - 1或者l = mid
此时为了防止死循环，计算mid时需要加1。

def binary_search_2(l, r):
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid): 
            l = mid
        else:
            r = mid - 1
    return l
    
mid需要加1的原因：当 check(mid) = true 时，l = mid and r = mid + 1，mid = l + r >> 1 = mid，则死循环
"""
