"""

1.	Calculate the sum of all the elements of x that are positive (>0) and store this sum in the variable possum;
2.	Count the number of elements of X that are negative (<0) and store this count in the variable negcount;
3.	Count the number of positive elements of X that are odd numbers and store this count in the variable oddcount.
    Note that an odd number is one that does not divide exactly by 2 and so has a least significant bit of 1
4.	Detect if possum has overflowed and set overflow to 1 if it has (0 otherwise).
    In this case the value of possum will be incorrect but your program should continue,
    even if this is detected, to allow oddcount and negcount to be computed.
    Note that on adding 2 positive two's complement numbers,
    an overflow occurs if and only if the sum becomes negative.
    Also note that oddcount and negcount cannot overflow given the constraints on array size.

    检测possum是否溢出，如果溢出设置为1(否则设置为0)。
    在这种情况下，possum的值将不正确，但您的程序应该继续，即使检测到这一点，也允许计算oddcount和negcount。
    注意，当两个正数相加时，当且仅当和变为负时，就会发生溢出。
    还要注意，给定数组大小的约束，oddcount和negcount不能溢出。

    X = [3, -6, 27, 101, 50, 0, -20, -21, 19, 6, 4, -10]
"""
N = 16
M = 2 ** (N - 1)

possum = 0  # 正数的总和
oddcount = 0  # 负数个数
negcount = 0  # 正奇数的个数

if __name__ == '__main__':
    # [3, -6, 27, 101, 50, 0, -20, -21, 19, 6, 4, -10, 32557]
    X = list(map(int, input().split(', ')))
    for x in X:
        possum = (possum + x if possum + x < M else 1) if x > 0 else possum
        oddcount += 1 if x < 0 else 0
        negcount += 1 if x > 0 and x & 1 == 1 else 0

    print(possum, oddcount, negcount)
