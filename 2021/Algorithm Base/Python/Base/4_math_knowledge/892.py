"""
台阶-Nim游戏
现在，有一个 n 级台阶的楼梯，每级台阶上都有若干个石子，其中第 i 级台阶上有 ai 个石子(i≥1)。

两位玩家轮流操作，每次操作可以从任意一级台阶上拿若干个石子放到下一级台阶中（不能不拿）。

已经拿到地面上的石子不能再拿，最后无法进行操作的人视为失败。

问如果两人都采用最优策略，先手是否必胜。

输入格式
第一行包含整数 n。

第二行包含 n 个整数，其中第 i 个整数表示第 i 级台阶上的石子数 ai。

输出格式
如果先手方必胜，则输出 Yes。

否则，输出 No。

数据范围
1≤n≤105,
1≤ai≤109
输入样例：
3
2 1 3
输出样例：
Yes
==============================================================
解法：

    将奇数台阶看做一个经典的Nim游戏，如果先手时奇数台阶上的值的异或值为0，则先手必败，反之必胜

证明：

    先手必胜 -> 可以走到某一个必败状态（即第一步走到一个必败状态）
            a1 ^ a2 ^ ... ^ an ≠ 0

    先手必败 -> 走不到任何一个必败状态（即第一步就是必败状态）
            a1 ^ a2 ^ ... ^ an = 0

    先手时，如果奇数台阶异或值 != 0，根据经典Nim游戏，先手总有一种方式使奇数台阶异或值 = 0，即为先手必胜状态
    轮到后手：
        ① 当后手移动偶数台阶上的石子时，先手只需将对手移动的石子继续移到下一个台阶，这样奇数台阶的石子相当于没变，
            于是留给后手的又是奇数台阶异或值 = 0的状态
        ② 当后手移动奇数台阶上的石子时，留给先手的奇数台阶异或值 != 0，根据经典Nim游戏，先手总能找出一种方案使奇数台阶异或值 = 0

    因此无论后手如何移动，先手总能通过操作把奇数异或值 = 0的情况留给后手
    最终当奇数台阶全为 0时，只留下偶数台阶上有石子。
    （核心就是：先手总是把奇数台阶异或为0的状态留给对面，即总是将必败态交给对面）

    因为偶数台阶上的石子要想移动到地面，必然需要经过偶数次移动，
    又因为奇数台阶全 0的情况是留给后手的，
    因此先手总是可以将石子移动到地面，
    当将最后一个（堆）石子移动到地面时，后手无法操作，即后手失败。
    因此如果先手时奇数台阶上的值的异或值 != 0，则先手必胜，反之必败！
"""
if __name__ == '__main__':
    n = int(input())
    L = list(map(int, input().split()))
    res = 0
    for i in range(len(L)):
        if i & 1 == 0:  # (i + 1) & 1 == 1
            res ^= L[i]
    print('Yes' if res >= 1 else 'No')  # res != 0