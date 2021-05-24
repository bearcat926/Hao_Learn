"""
排列数字
给定一个整数n，将数字1~n排成一排，将会有很多种排列方法。

现在，请你按照字典序将所有的排列方法输出。

输入格式
共一行，包含一个整数n。

输出格式
按字典序输出所有排列方案，每个方案占一行。

数据范围
1 ≤ n ≤ 7
输入样例：
3
输出样例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

DFS - 深度优先搜索

    思考核心 - 顺序 -> 暴搜
    实现方法 -> 回溯（恢复现场）, 本质是递归

"""
N = 7
Path = [0] * (N + 1)  # 当前路径[1-n]
Bool = [False] * (N + 1)  # 查看某数[1-n]是否在被使用


def dfs(i, n):
    if i == n:  # 到末尾了，打印
        for x in Path[:n]:
            print(x, end=' ')
        print()
        return
    j = 1
    while j <= n:  # [1-n]
        if Bool[j] is not True:  # 当前j没有被使用
            Path[i] = j  # 当前路径上为j
            Bool[j] = True  # 表示j正在被使用
            dfs(i + 1, n)  # 去下一路径做dfs
            Bool[j] = False  # j使用完了
        j += 1


if __name__ == '__main__':
    n = int(input())
    dfs(0, n)
