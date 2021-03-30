"""
筛法

    把从2到N的一组正整数从小到大按顺序排列。
    从中依次删除2的倍数、3的倍数、5的倍数，直到√N的倍数为止，
    剩余的即为2~N之间的所有素数。

    时间复杂度计算

        朴素筛法

            n / 2 + n / 3 + ... + n / n = n * (1/2 + 1/3 + ... + 1/n)

            调和级数 -> 当n -> ∞时, 1 + 1/2 + 1/3 + ... + 1/n = ln_n + c , c为欧拉常数

            因为 ln_n < log_2_n, 所以总复杂度约为 O(nlog_n)


        优化1 - 质数的倍数都是合数 -> 埃氏筛法

            根据质数定律：1 ~ n中 有 n / ln_n 个质数

            时间复杂度小于 n / ln_n * ln_n = n

            实际复杂度为 O(nlog_log_n)

        优化2 - 任何一个合数都有最小质因子 -> 线性筛法

            对于一个合数x, 假设pj是x的最小质因子,
            当i枚举到x / pj的时候, x就会被筛掉, 即n只会被最小质因子筛掉


=======================================
筛质数

给定一个正整数 n，请你求出 1∼n 中质数的个数。

输入格式
共一行，包含整数 n。

输出格式
共一行，包含一个整数，表示 1∼n 中质数的个数。

数据范围
1≤n≤106
输入样例：
8
输出样例：
4
"""
N = 10 ** 6 + 10
PRIME, ST = [0] * N, [False] * N
cnt = 0


def get_primes(x):
    global cnt
    i = 2
    while i <= x:
        if not ST[i]:  # 当前数字未被使用过, 则该数为质数
            PRIME[cnt] = i
            cnt += 1
        k = i
        while k <= x:
            ST[k] = True
            k += i
        i += 1
    print(cnt)


def get_primes_optimize_1(x):
    global cnt
    i = 2
    while i <= x:
        if not ST[i]:  # 当前数字未被使用过, 则该数为质数
            PRIME[cnt] = i
            cnt += 1
            k = i
            while k <= x:
                ST[k] = True
                k += i
        i += 1
    print(cnt)


def get_primes_optimize_2(x):
    global cnt
    i = 2
    while i <= x:
        if not ST[i]:  # 当前数字未被使用过, 则该数为质数
            PRIME[cnt] = i
            cnt += 1
        j = 0
        while PRIME[j] <= n / i:  # 循环 PRIME[j] * i < n 的部分
            """
                当 i % (PRIME[j]) == 0 时
                    PRIME[j]一定是i的最小质因子, PRIME[j]也一定是 PRIME[j] * i的最小质因子
                当 i % (PRIME[j]) != 0 时
                    PRIME[j]一定小于i的最小质因子, 而PRIME[j]一定是 PRIME[j] * i的最小质因子
            """
            ST[PRIME[j] * i] = True
            if i % (PRIME[j]) == 0:
                break
            j += 1
        i += 1
    print(cnt)


if __name__ == '__main__':
    n = int(input())
    # get_primes(n)
    # get_primes_optimize_1(n)
    get_primes_optimize_2(n)