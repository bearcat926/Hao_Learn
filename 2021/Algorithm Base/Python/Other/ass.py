"""
给一个日期：20200202

观察这个日期，同时满足两个特征：

1.左右对称

2.除数字0外，只有一个非零数字



编码实现以下两项：

1.输入任意日期，判断是否满足以上条件，测试用例：20200202，21211212

2.输出自19700101至今所有符合条件的日期

参考思路：

//还需要对输入进行校验，是否是正确的日期
"""
import time


def is_valid_date(str_date):  # 判断是否是一个有效的日期字符串
    try:
        time.strptime(str_date, "%Y-%m-%d")
        return True
    except Exception:
        return False


def check_date(start_year, end_year):
    for y in range(int(start_year), int(end_year)):
        year = str(y)
        re_year = ''

        stack = list(year)
        if stack.__contains__('0') and len(set(stack)) == 2:  # 检测是否除数字0外，只有一个非零数字
            while len(stack) != 0:  # 通过stack实现左右对称
                re_year += stack.pop()

            date = year + "-" + re_year[:2] + "-" + re_year[2:]  # 最终日期
            if is_valid_date(date):  # 检测日期是否有效
                print(date.replace("-", ""))


def check_date_2(year):
    prev_year = year[:4]
    next_year = year[4:]
    re_year = ''

    stack = list(prev_year)
    if stack.__contains__('0') and len(set(stack)) == 2:  # 检测是否除数字0外，只有一个非零数字
        while len(stack) != 0:  # 通过stack实现左右对称
            re_year += stack.pop()
        if next_year == re_year:
            date = prev_year + "-" + next_year[:2] + "-" + next_year[2:]  # 最终日期
            if is_valid_date(date):  # 检测日期是否有效
                return True
    return False


check_date("1970", "9999")
print(check_date_2("21211212"))
