"""
最长连续不重复子序列
给定一个长度为n的整数序列，请找出最长的不包含重复的数的连续区间，输出它的长度。

输入格式
第一行包含整数n。

第二行包含n个整数（均在0~100000范围内），表示整数序列。

输出格式
共一行，包含一个整数，表示最长的不包含重复的数的连续区间的长度。

数据范围
1 ≤ n ≤ 100000
输入样例：
5
1 2 2 3 5
输出样例：
3
"""
n = int(input())
L = list(map(int, input().split()))
S = [0] * (100000 + 10)

count = 0
j = 0
for i in range(n):
    S[L[i]] += 1
    while j < i and S[L[i]] > 1:  # 说明有重复数字出现，解决方法是移动j，同时将之前的数据从数组中剔除
        S[L[j]] -= 1
        j += 1
    count = max(count, i - j + 1)

print(count)

"""
双指针算法
j = 0
for i in range(n):
    while j < i and check(i, j):
        j += 1
        // 具体问题的逻辑
        
常见问题分类：
    (1) 对于一个序列，用两个指针维护一段区间
    (2) 对于两个序列，维护某种次序，比如归并排序中合并两个有序序列的操作
    
核心思想：
    将O(n^2)的朴素算法优化到O(n)
    
"""
