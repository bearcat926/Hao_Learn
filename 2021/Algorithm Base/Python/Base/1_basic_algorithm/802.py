"""
区间和
假定有一个无限长的数轴，数轴上每个坐标上的数都是0。

现在，我们首先进行 n 次操作，每次操作将某一位置x上的数加c。

接下来，进行 m 次询问，每个询问包含两个整数l和r，你需要求出在区间[l, r]之间的所有数的和。

输入格式
第一行包含两个整数n和m。

接下来 n 行，每行包含两个整数x和c。

再接下里 m 行，每行包含两个整数l和r。

输出格式
共m行，每行输出一个询问中所求的区间内数字和。

数据范围
−109 ≤ x ≤ 10^9,
1 ≤ n,m ≤ 10^5,
−109 ≤ l ≤ r ≤ 109,
−10000 ≤ c ≤ 10000
输入样例：
3 3
1 2
3 6
7 5
1 3
4 6
7 8
输出样例：
8
0
5

1. 将所有的坐标映射到，离散化之后的数组上
"""
n, m = map(int, input().split())
N = 100000  # n 和 m 的取值范围
add = []  # 存储插入操作的二元组
query = []  # 存储查询操作的二元组
alls = []  # 存储插入和查询的所有坐标，并完成 alls[index] = x 的映射
A = [0] * (N * 3 + 10)  # alls最大可以存储了 n + 2 * m个坐标
S = [0] * (N * 3 + 10)  # 前缀和数组的大小也要随A适应


# 二分查找
def find(x):
    l = 0
    r = len(alls) - 1
    while l < r:
        mid = l + r + 1 >> 1
        if alls[mid] >= x:
            r = mid - 1
        else:
            l = mid
    return l + 1  # 因为要计算前缀和，所以加1保证索引从1开始 => B[1] = B[0] + A[1]


if __name__ == '__main__':
    for i in range(n):
        x, c = map(int, input().split())
        add.append((x, c))
        alls.append(x)

    for j in range(m):
        l, r = map(int, input().split())
        query.append((l, r))
        alls.append(l)
        alls.append(r)

    # 1. 进行映射 - 将all数组去重后排序
    alls = list(sorted(set(alls)))

    # 2. 插入数据
    for x, c in add:
        index = find(x)
        A[index] += c

    # 3. 计算前缀和
    for i in range(1, len(alls) + 1):
        S[i] = S[i - 1] + A[i]

    # 4. 输出结果 l ~ r 的前缀和 => S[index_l] - S[index_r - 1]
    for l, r in query:
        print(S[find(r)] - S[find(l) - 1])