"""
食物链
动物王国中有三类动物 A,B,C，这三类动物的食物链构成了有趣的环形。

A 吃 B，B 吃 C，C 吃 A。

现有 N 个动物，以 1∼N 编号。

每个动物都是 A,B,C 中的一种，但是我们并不知道它到底是哪一种。

有人用两种说法对这 N 个动物所构成的食物链关系进行描述：

第一种说法是 1 X Y，表示 X 和 Y 是同类。

第二种说法是 2 X Y，表示 X 吃 Y。

此人对 N 个动物，用上述两种说法，一句接一句地说出 K 句话，这 K 句话有的是真的，有的是假的。

当一句话满足下列三条之一时，这句话就是假话，否则就是真话。

当前的话与前面的某些真的话冲突，就是假话；
当前的话中 X 或 Y 比 N 大，就是假话；
当前的话表示 X 吃 X，就是假话。
你的任务是根据给定的 N 和 K 句话，输出假话的总数。

输入格式
第一行是两个整数 N 和 K，以一个空格分隔。

以下 K 行每行是三个正整数 D，X，Y，两数之间用一个空格隔开，其中 D 表示说法的种类。

若 D=1，则表示 X 和 Y 是同类。

若 D=2，则表示 X 吃 Y。

输出格式
只有一个整数，表示假话的数目。

数据范围
1≤N≤50000,
0≤K≤100000
输入样例：
100 7
1 101 1
2 1 2
2 2 3
2 3 3
1 1 3
2 3 1
1 5 5
输出样例：
3
"""
N = 50000
P = [0]
D = [0] * (N + 10)
count = 0


def get_root(x):
    if P[x] != x:
        # 先保存t的原因是 需要利用递归先计算D[x]的值
        t = get_root(P[x])
        # D[x] => x到根节点的距离，因为P[x]会在路径压缩之后变成父节点，所以需要在这之前计算D[x]
        D[x] += D[P[x]]
        P[x] = t
    return P[x]


"""
    食物链（带权并查集）
    
    关系传递的本质实际上是向量的运算。
    
            a(0)      3
           /
          b(1)       2
         /
        c(2)        1
       /
      a’(0)        3   
    
    说明：b吃a, c吃b, a’吃c, a 和 a’是同类       
    所以 b % 3 = a % 3 + 1，即 b可以吃a      
        a' % 3 = a % 3, 即 a 和 a’是同类    
        
    在此不可以使用b % 3 - 1 = a % 3 ，
    因为当b = 0时，(b - 1) % 3 = -1 % 3 = -1 != a
"""


def merge(r_x, r_y, x, y, b):
    if r_x != r_y:  # 根节点不同，需要merge
        """
            同类合并：            
            设 (D[x] + ?) % 3 = D[y] % 3 
            若使 D[x] + ? = D[y]，也可使等式成立
            则 ? = D[y] - D[x]
            
            捕食关系合并：            
            因为 x 可以吃 y
            设 (D[x] + ?) % 3 = D[y] % 3 + 1
            若使 D[x] + ? = D[y] + 1，也可使等式成立
            则 ? = D[y] - D[x] + 1
            
            注意：进行向量差比较时，使用的是D[x]和D[y]
        """
        P[r_x] = r_y  # 根节点变为r_y
        D[r_x] = D[y] - D[x] + b  # x的 原始根节点 到 现在根节点 的距离根节点


def check_same(r_x, r_y, x, y):  # 检查 X 和 Y 是否是同类
    global count
    count += 1 if r_x == r_y and D[x] % 3 != D[y] % 3 else 0
    merge(r_x, r_y, x, y, 0)


def check_eat(r_x, r_y, x, y):  # 检查 X 是否可以吃 Y
    global count
    count += 1 if r_x == r_y and D[x] % 3 != (D[y] + 1) % 3 else 0
    merge(r_x, r_y, x, y, 1)


if __name__ == '__main__':

    n, k = map(int, input().split())
    P += [x for x in range(1, n + 1)]
    for i in range(k):
        op, *x = map(int, input().split())
        # 边缘检测
        if x[0] > n or x[1] > n:
            count += 1
            continue
        # 此处的get_root只能使用一次，因为每次调用函数会重新计算D[x]的值，是路径变得更长
        r_x, r_y = get_root(x[0]), get_root(x[1])
        if op == 1:
            check_same(r_x, r_y, x[0], x[1])
        elif op == 2:
            check_eat(r_x, r_y, x[0], x[1])
    print(count)
