"""
区间合并
给定 n 个区间 [li,ri]，要求合并所有有交集的区间。

注意如果在端点处相交，也算有交集。

输出合并完成后的区间个数。

例如：[1,3]和[2,6]可以合并为一个区间[1,6]。

输入格式
第一行包含整数n。

接下来n行，每行包含两个整数 l 和 r。

输出格式
共一行，包含一个整数，表示合并区间完成后的区间个数。

数据范围
1 ≤ n ≤ 100000,
−10^9 ≤ li ≤ ri ≤ 10^9
输入样例：
5
1 2
2 4
5 6
7 8
7 9
输出样例：
3
"""
n = int(input())
P = []

for i in range(n):
    l, r = map(int, input().split())
    P.append((l, r))

P = sorted(P, key=lambda x: x[0])

if __name__ == '__main__':
    st = ed = -1000000000
    count = 0
    for l, r in P:
        # 1. l, r <= ed -> 忽略
        if l <= ed < r:  # 2. l <= ed < r -> ed = r
            ed = r
        elif ed < l:  # 3. ed < l -> count += 1 and st, ed = l, r
            count += 1
            st, ed = l, r
    if st == -1000000000:
        count += 1
    print(count)
