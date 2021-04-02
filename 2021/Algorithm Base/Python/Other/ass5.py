"""
t = 1, 3 , 2 , 1

3 => 4
2 => 5
1 => 6

dy = {-1, 0, 1, 0}
dx = {0, 1, 0, -1}

1. 创建地图
          1 1 1 1 1 1 1 1 1
          1 0 - 0 - 0 - 0 1
          1 | 1 1 1 1 1 | 1
          1 0 1 0 - 0 1 0 1
          1 | 1 1 1 | 1 | 1
          1 0 - 0 - 0 1 0 1
          1 1 1 1 1 1 1 | 1
                        0 1


i = 2
res = 1
while q < res + 2 * (i - 1):
res += 2 * i - 1
i += 1

3 3

2 3 3  4
3 5 7  6
4 7 13 8
5 9 21

2 off = 3 , res = 0, limit = 3
3 off = 5 , res = 2, limit = 7
4 off = 7 , res = 6, limit = 13
5 off = 9 , res = 12, limit = 21
6 off = 11, res = 20, limit = 31

off = 2 * i - 1
res = (i - 1) * (i - 2)
limit = res + off
start = res + 1
end = limit

i = 2
off, res, limit = 0, 0, 3
while q < limit:
    off = 2 * i - 1
    res = (i - 1) * (i - 2)
    limit = res + off

start = res + 1
# 往前滚就行了

t = 3, f = 2, r = 1

3 1 4 6
6 3 1 4
6 2 1 5
5 6 2 1


i = 2, i & 1 = 0, 右1, 下1 => 双数右下，各i-1次
i = 3, i & 1 = 1, 左2, 上2 => 单数左上


# init
i = 2
s, t, f, r = 7, 3, 2, 1
# 先右
X = [t, r, s - t, s - r]
t = X[(0 - (i - 1)) % 4]
r = X[(1 - (i - 1)) % 4]
# 再下
Y = [t, f, s - t, s - f]
print(Y)
t = Y[(0 - (i - 1)) % 4]
f = Y[(1 - (i - 1)) % 4]
print(t, f, r)
"""
if __name__ == '__main__':
    q = int(input())
    if q > 0:
        i, res, off, limit, start, end = 2, 0, 3, 3, 1, 3
        s, t, f, r = 7, 3, 2, 1
        o_t, o_f, o_r = 3, 2, 1
        while q > limit:
            off = 2 * i - 1
            res = (i - 1) * (i - 2)
            limit = res + off
            start = res + 1
            end = limit

            if q == start:
                print(t, f, r)

            o_t, o_f, o_r = t, f, r
            if i & 1 == 0:
                # 先右
                X = [t, r, s - t, s - r]
                t = X[(0 - (i - 1)) % 4]
                r = X[(1 - (i - 1)) % 4]
                # 再下
                Y = [t, f, s - t, s - f]
                t = Y[(0 - (i - 1)) % 4]
                f = Y[(1 - (i - 1)) % 4]
            else:
                # 先左
                X = [t, s - r, s - t, r]
                t = X[(0 - (i - 1)) % 4]
                r = X[(3 - (i - 1)) % 4]
                # 再上
                Y = [t, s - f, s - t, f]
                t = Y[(0 - (i - 1)) % 4]
                f = Y[(3 - (i - 1)) % 4]

            if q == end:
                print(t, f, r)
                break

            i += 1
        # # 区间内
        if q <= limit:
            if i != 2:
                i -= 1
            d = q - start  # 需要移动的步数
            off = d - (i - 1)  # 超过i-1的部分
            d = i - 1 if d >= i - 1 else d
            if i & 1 == 0:
                # 先右
                X = [o_t, o_r, s - o_t, s - o_r]
                o_t = X[(0 - d) % 4]
                o_r = X[(1 - d) % 4]
                if off > 0:  # 再下
                    Y = [o_t, o_f, s - o_t, s - o_f]
                    o_t = Y[(0 - off) % 4]
                    o_f = Y[(1 - off) % 4]
            else:
                # 先左
                X = [o_t, s - o_r, s - o_t, o_r]
                o_t = X[(0 - d) % 4]
                o_r = X[(3 - d) % 4]
                if off > 0:  # 再上
                    Y = [o_t, s - o_f, s - o_t, o_f]
                    o_t = Y[(0 - off) % 4]
                    o_f = Y[(3 - off) % 4]
            print(o_t, o_f, o_r)