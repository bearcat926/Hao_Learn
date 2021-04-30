"""
筛法求欧拉函数
给定一个正整数 n，求 1∼n 中每个数的欧拉函数之和。

输入格式
共一行，包含一个整数 n。

输出格式
共一行，包含一个整数，表示 1∼n 中每个数的欧拉函数之和。

数据范围
1≤n≤106
输入样例：
6
输出样例：
12
=======================================
1. 朴素：筛去2 ~ √N的倍数
2. 埃氏：质数的倍数是合数
3. 线性：通过最小质因子筛去合数, 可以保证筛法整体呈线性
"""
N = 10 ** 6 + 10
PHI = [0] * N
PRIME = [0] * N
ST = [False] * N
cnt = 0


def euler(n):
    global cnt
    PHI[1] = 1
    i = 2
    while i <= n:
        if not ST[i]:
            PRIME[cnt] = i
            PHI[i] = i - 1
            cnt += 1
        j = 0
        while PRIME[j] <= n // i:
            ST[PRIME[j] * i] = True
            if i % PRIME[j] == 0:
                PHI[PRIME[j] * i] = PRIME[j] * PHI[i]
                """
                    根据欧拉函数，1∼N 中与 N互质的数的个数, 只与其所有质因数相关
                    由于 ϕ(i) 的质因数都是 ϕ(PRIME[j] * i) 的质因数，
                    且 i % PRIME[j] == 0 时, PRIME[j] 是 i 的质因数 => ϕ(i)中包含(1 - 1//PRIME[j])
                    因此 ϕ(PRIME[j] * i) = PRIME[j] * ϕ(i)
                """
                break
            # PHI[PRIME[j] * i] = PRIME[j] * PHI[i] * (1 - 1 // PRIME[j])
            PHI[PRIME[j] * i] = (PRIME[j] - 1) * PHI[i]
            j += 1
        i += 1
    res = 0  # 可能会大于int.max
    for i in range(1, n + 1):
        res += PHI[i]
    print(res)


if __name__ == '__main__':
    euler(int(input()))
