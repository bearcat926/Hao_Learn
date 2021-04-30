# Returns the list of all lists of the form [L[i_0], ..., L[i_k]] such that:
# - i_0 < ... < i_k
# - L[i_0] < ... < L[i_k]
# - there is NO list of the form [L[j_0], ..., L[j_k']] such that:
#   * j_0 < ... < j_k'
#   * L[j_0] < ... < L[j_k']
#   * {i_0, ..., i_k} is a strict subset of {j_0, ..., j_k'}.
#
# The solutions are output in lexicographic order of the associated tuples
# (i_0, ..., i_k).
#
# Will be tested on inputs that, for some of them, are too large for a brute
# force approach to be efficient enough. Think recursively.
#
# You can assume that L is a list of DISTINCT integers.
from typing import List


def f(L):
    '''
    >>> f([3, 2, 1])
    [[3], [2], [1]]
    >>> f([2, 1, 3, 4])
    [[2, 3, 4], [1, 3, 4]]
    >>> f([4, 7, 6, 1, 3, 5, 8, 2])
    [[4, 7, 8], [4, 6, 8], [4, 5, 8], [1, 3, 5, 8], [1, 2]]
    >>> f([3, 4, 6, 10, 2, 7, 1, 5, 8, 9])
    [[3, 4, 6, 10], [3, 4, 6, 7, 8, 9], [3, 4, 5, 8, 9], [2, 7, 8, 9], \
[2, 5, 8, 9], [1, 5, 8, 9]]
    '''
    solutions = []
    P = []  # 临时数组path
    S = []  # 字符串结果集
    # INSERT YOUR CODE HERE
    dfs(L, P, S)  # 使用 dfs构造所有上升子序列
    S = sorted(S, key=lambda x: len(x), reverse=True)  # 将所有子序列按长度倒序排序
    for e in S:  # 枚举S中所有字符串，并删除由字符串组成的子字符串，直至遍历完成
        arr = e.split(' ')
        for i in range(1, (1 << len(arr)) - 1):  # 使用二进制位运算枚举所有情况, -1 确保不删除自身
            t = i
            k = len(arr) - 1
            s = []
            while t != 0:
                if t & 1 == 1:
                    s.append(arr[k])  # 在临时数组s中放入符合条件的数
                k -= 1
                t >>= 1
            str = ''.join(['%s ' % s[e] for e in range(len(s) - 1, -1, -1)]).rstrip()  # 倒序构造str
            if S.__contains__(str):  # 存在及删除
                S.remove(str)
    solutions = [list(map(int, e.split(' '))) for e in S]  # 将字符串还原为整数数组
    solutions = sorted(solutions, key=lambda x: [i for i in x], reverse=True)  # 按位倒序排序
    return solutions


# POSSIBLY DEFINE ANOTHER FUNCTION
def dfs(nums: List[int], path: List[int], res: List[str]) -> None:
    if len(path) >= 1:
        res.append(''.join(['%s ' % e for e in path]).rstrip())  # 将整数数组构造为字符串，便于使用
    m = set()
    for i in range(len(nums)):
        if m.__contains__(nums[i]):  # 去重
            continue
        if not path or nums[i] >= path[-1]:  # 路径为空 或 当前数字大于末尾数字
            m.add(nums[i])
            dfs(nums[i + 1:], path + [nums[i]], res)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
