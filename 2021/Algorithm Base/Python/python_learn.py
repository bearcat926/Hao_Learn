# print("Hello World")

# 字符串 单引号 双引号皆可
# message = "Hello World"
# message = 'Hello World dan yin hao'
# print(message)

# 首字母大写
# print(message.title())
# 全大写
# print(message.upper())
# 全小写
# print(message.lower())

# 合并字符串
# first_name = "chen"
# last_name = "xiao han"
# full_name = first_name + " " +last_name
# print(full_name)

# \t 制表符 \n 换行符
# print("Languages:\n\tPython\n\tJava")

# 删除空白
# favorite_language = " python "
# print(favorite_language.lstrip())
# print(favorite_language.rstrip())
# print(favorite_language.strip())

# 加减乘除
# 取模运算
# print(3 % 2)

# 整除运算
# print(7 // 3)

# **乘方计算
# print(3 ** 3)

# 赋值运算
# i = 1
# i += 5
# print(i)
# i -= 1
# print(i)
# i *= 5
# print(i)
# i /= 5
# print(i)
# i %= 3
# print(i)
# i **= 3
# print(i)
# i //= 2
# print(i)

# 浮点数 ，结果包含的小数位数可能是不确定的
# print(0.1 + 0.1)
# print(0.2 + 0.1)

# 进制转换
# 十进制转二进制
# print(bin(2))
# 十进制转八进制
# print(oct(8))
# 十进制转十六进制
# print(hex(16))

# int(x[, base])  # 将x转换为一个整数
# long(x[, base])  # 将x转换为一个长整数
# float(x)  # 将x转换到一个浮点数
# complex(real[, imag])  # 创建一个复数
# str(x)  # 将对象 x 转换为字符串
# repr(x)  # 将对象 x 转换为表达式字符串
# eval(str)  # 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)  # 将序列 s 转换为一个元组
# list(s)  # 将序列 s 转换为一个列表
# chr(x)  # 将一个整数转换为一个字符
# unichr(x)  # 将一个整数转换为Unicode字符
# ord(x)  # 将一个字符转换为它的整数值
# hex(x)  # 将一个整数转换为一个十六进制字符串
# oct(x)  # 将一个整数转换为一个八进制字符串

# 二进制转十进制 注意被转换的值为字符串
# print(int('10',2))
# 八进制转十进制
# print(int('10',8))
# 十六进制转十进制
# print(int("10",16))

# 按位与运算 &
# i = 11
# j = 2
# z = i & j
# print(bin(i))
# print(bin(j))
# print(z)

# 按位或运算
# i = 11
# j = 2
# z = i | j
# print(bin(i))
# print(bin(j))
# print(z)

# 按位异或运算
# i = 11
# j = 2
# z = i ^ j
# print(bin(i))
# print(bin(j))
# print(z)

# 按位取反运算，负数减一
# i = 11
# z = ~i
# print(bin(i))
# print(bin(z))

# 左移运算符
# i = 11
# z = i << 2
# print(bin(i))
# print(z)
# print(bin(z))

# 右移运算符
# i = 11
# z = i >> 2
# print(bin(i))
# print(z)
# print(bin(z))

# 注释
# 单行注释
'''
多行注释1
'''
"""
多行注释2
"""

# 条件控制
'''
1.
    if 条件:
        语句
2.
    if 条件:
        语句
    else:
        语句   
3.
    if 条件:
        语句
    elif 条件:
        语句
    else:
        语句     
    
'''
# flag = False
# if flag:
#     flag = True
# elif ~flag:
#     flag = False
# else:
#     flag = 1

# 输入语句
# inStr = input("请输入字符串：")

# 使用函数str()避免类型错误
# age = 23
# message = "Happy " + str(age) + "rd Birthday"
# print(message)

# 列表
# bicycles = ["trek", "cannondale" ,"redline", "specialized"]
# print(bicycles)
# print(bicycles[0])
# print(bicycles[-1])

# 字符串声明
# s = 'Hello Python'
# print(s)
# s = "Hello Python"
# print(s)
# s = """Hello
# Python"""
# print(s)

# 字符串的操作
# s = 'Hello Python'
# print(s[0])
# '''
# Hello Python
# 0123456789
# '''

# 访问字符串的子串（左闭右开）  -  切片操作
# print(s[0:5])

# 字符串相加计算
# s1 = "Hello"
# s2 = "Python"
# print(s1 + " " +s2)

# 字符串更新操作
# s1 = "Hello String"
# s2 = "Python"
# print(s1[:6] + s2)

# 字符串的成员运算
# s1 = "Hello String"
# s2 = "H"
# print(s2 in s1) # 包含运算
# print(s2 not in s1) # 不包含运算

# 转义字符
# print("\'")
# print("\"")
# print("Hello\nPython")
# print("Hello\tPython")
# print("Hello\rPython") # 回车：光标到行首，打印\r之后的内容
# 原始字符串
# print(r"Hello\nPython")
# print(R"Hello\nPython")
# print("Hello\\nPython")

# 字符串的格式化输出
# print("我叫%s，今天是我第%d天学习Python"%("小明",10))

# 字符串的内建函数
# # 查找字符串
# s = "Hello Python".find("Hello")
# print(s)
# # 转换成小写字符
# print("Hello Python".lower())
# # 转换成大写字符
# print("Hello Python".upper())
# # 返回字符串长度，返回的是自然长度
# print("Hello Python".__len__())
# # 判断字符串是否只包含空格
# print(" ".isspace())
# print("a ".isspace())
# # 字符串替换
# print("Hello Python".replace("o", "ee"))

# python自带的学习文档
# python3 -m pydoc -p 8888

'''
列表：一组数据
list是有序的序列
序列中的每个元素分配一个数字，即索引，位置角标，坐标
也是从0开始
'''

# list1 = ['build',13,'love',18,'defend',15]
# print(type(list1))
# print(list1)
#
# # 访问列表
# print(list1[0])
# print(list1[2:])
# print(list1[1:3])
#
# # 更新
# list1[1] = 14
# print(list1)
#
# # 添加
# list1.append("army")
# list1.append(20)
# print(list1)
# list1 = list1 + ["yep", 25]
# print(list1)
#
# # 删除
# del list1[4]
# print(list1)

# 嵌套
# list1 = [['build','love','defend'], [12, 14 , 18]]
# print(list1)
# print(list1[0][0])
#
# # 返回列表元素的个数
# count = len(list1)
# print(count)
# print(len(list1[0]))
#
# # 移除列表中的元素，并且返回这个值
# l = list1.pop(1)
# print(l)
# print(list1)
#
# # 对列表中的元素进行排序
# list1 = [12, 11, 13]
# list1.sort()
# print(list1)
#
# # 查找列表中第一个匹配的元素的索引值
# list1 = [12, 11, 13]
# i = list1.index(11)
# print(i)

'''
元组：在一个小括号内包裹着
不能修改
'''
# l = [1,2,3]
# t = (1,2,3)
# print(type(l))
# print(type(t))
#
# print(t[0])
# print(t[2:])

'''
集合，是一个无序的不重复元素的序列
两种声明方法
1.使用{}
2.set()
'''
# set_param = {"1","2","3","3"}
# print(set_param)
#
# # 判断元素是否在集合内
# print("11" in set_param)
# print("1" in set_param)

# 两个集合间的运算
# a = set('abcdef')
# b = set('abcxyz')
# print(a)
# print(b)
# print(a & b)
# print(a | b)
# print(a ^ b)

# # 集合添加元素
# my_set = set((1,2,3))
# my_set.add("4")
# print(my_set)
#
# # 移除指定元素
# my_set.remove(2)
# print(my_set)
#
# # 随机移除一个元素
# pop_param = my_set.pop()
# print(pop_param)
# print(my_set)
#
# # 计算集合中的元素个数
# print(len(my_set))
#
# # 清空集合
# my_set.clear()
# print(my_set)

'''
字典：一种可变容器类型，也是可以存储任意类型的对象
'''
# d = {'1':1,"2":2,"3":3}
# print(d)
#
# # 访问
# keys = d.keys()
# print(keys)
# print(d.values())
# print(d["1"])
#
# # 添加
# d["4"] = 4
# print(d)
#
# # 更新
# d["3"] = 33
# print(d)
#
# # 删除
# del d["3"]
# print(d)
#
# # 判断键是否在字典中
# print('3' in d)
# print('2' in d)
#
# # 清空
# d.clear()
# print(d)

'''
条件控制
1.比较运算符
 ==
 >
 <
 >=
 <=
 !=
2.成员运算符
 in
 not in
3.逻辑运算符
 and or not
4.身份运算符
 is
 is not
'''
# ASCII码表转换 A-Z(65-90), a-z(97-122)
# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))
# print(chr(76))

# house_person = ['建国', '爱国', '卫国']
#
# if '建国' in house_person and '卫国'in house_person\
#     and '爱国' in house_person:
#     print("斗地主")
# else:
#     print("打游戏")

# 关于True和False的讨论
# print(True and False)
# print(True or False)
# print(not True)

# print(2 and 0)
# print(2 or 0)
# print(not 2)
'''
1其实是代表了True 0代表了False
and和or的逻辑判断是短路的，
'''
# print(0 and 4 and 5)
# print(3 or 4 or 5)

# i = 1
# j = 1
# print(i == j)
# print(i is j)
# print(id(i))
# print(id(j))
#
# j = j + 1
# print(id(j))

# list_1 = [1,2,3]
# list_2 = [1,2,3]
# print(list_1 == list_2)
# print(list_1 is list_2)
# print(id(list_1))
# print(id(list_2))

'''
运算符的优先级
'''

# 循环
# i = 1
# while i < 10:
#     print("循环")

# while 循环
# n = 1
# count = 0
# while n <= 100:
#     count += n
#     n += 1
# print(count);

# for循环
# list1 = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for i in list1:
#     count += i
# print(count)
#
# count = 0
# for i in range(11): # range(11) = [1,11)
#     count += i
# print(count)

'''
循环的中断
break continue
'''
# while True:
#     print(1)
#     break
#     print(2)
#
# while True:
#     print(1)
#     continue
#     print(2)

# i = 1
# while True:
#     print("外层循环1")
#     while True:
#         print("内层循环")
#         break
#     print("外层循环2")
#     # break
#     if i == 1:
#         print("外层循环3")
#         break

'''
1.冒泡排序

'''

# nums = [3, 1, 25, 10, 15, 6, 8]
# for i in range(len(nums) - 1):
#     for j in range(len(nums) - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         print("第" + str(j) + "次内循环" + str(nums))
#     print("第" + str(i) + "次外循环" + str(nums))


'''
工程结构：包 -> 模块 -> 类 -> (方法 -> 变量)，变量
编码规范：
    包：使用小写字母命名，如果有多个单词，则用下划线分隔
    模块：使用小写字母命名，如果有多个单词，则用下划线分隔
    类：使用驼峰命名法命名，如果有多个单词，则首字母大写，私有类用下划线开头
    变量：使用小写字母命名，如果有多个单词，则用下划线分隔，私有变量用下划线开头
    常量：全部使用大写字母命名，如果有多个单词，则用下划线分隔，私有常量用下划线开头
特殊模块 - __init__.py：
    只有包含了__init__.py模块的文件夹才能成为包（标记）
    __init__.py是在模块导入时运行的（运行）
    有引入的先后顺序

导包路径：
    包; 
    import part
    模块：
    from part.my_package import init_test
    from .my_package import init_test 
    import part.my_package.init_test as p // as 可以定义前缀名
    p.func
    
    .代表当前路径，..代表上一层路径
    后导入的路径会覆盖之前导入的
'''

'''
函数定义的格式
'''
# def my_func():
#     pass # 占位符

# 函数的参数
# 必须参数
# def my_func_with_param(p1, p2):
#     print(p1, p2)
#
# my_func_with_param(1, 2)

'''
形参： 形式参数，只是意义上的一种参数，在定义的时候不占内存地址
实参： 实实在在的参数，是实际占用内存地址的
'''
# 关键字参数： 是在调用的时候指定参数名称，可以不按顺序传参数
# def my_func_with_params(name, age):
#     print("我叫" + name  + "，今年" + str(age) + "岁。")
#
# my_func_with_params(age = 50, name = "zhang")

# 默认参数： 如果调用者没有传值，就使用默认值，可以不指定名字
# def my_func_with_param(name = "狗蛋", age = 50):
#     print(name + "来了，他今年：" + str(age) + "岁!")
#
# my_func_with_param()
# my_func_with_param("zhang", 49)

# 参数混合使用
# 混合使用时，非默认参数必须在默认参数的前边，如下sex
# def my_func_with_param(name,age = 50,sex):
#     print(name + "来了，他今年" + str(age) + "岁！")
#
# my_func_with_param(name="tang")
# my_func_with_param(name="liu", age = 70)

'''
函数的返回值
'''
# def func_with_return():
#     print("1")
#
# p = func_with_return()
# print(p)
# print(type(p))
#
# def func_with_return(): # 重写
#     return 1
#
# p = func_with_return()
# print(p)
# print(type(p))
#
# def func_with_return(p): # 重载
#     return p
#
# p = func_with_return("hahahh")
# print(p)
# print(type(p))

# 多个返回值
# def func_with_return(name, age):
#     return name,age
#
# n, a = func_with_return("zhang", 39)
# print(n, a)
# print(type(n), type(a))
#
# s = func_with_return("zhang", 39)
# print(s)
# print(type(s))

# 返回一个函数
# def func_with_return2(x):
#     if x == 2:
#         def inner_func(y):
#             return y * y
#     if x == 3:
#         def inner_func(y):
#             return y * y * y
#     return inner_func
#
# calc = func_with_return2(3)
# print(calc(4))

'''
递归
重点要明确递归结束的条件
写法简洁，但效率低
要求：每次递归的时候，规模都要有所缩小
现象：每两次相邻的调用，前一次都要为后一次作准备，即前一次运算的结果，是下一次运算的条件
'''
# def my_func(x): # 998为止，python的自我保护机制 - 有最大递归深度
#     print(x)
#     my_func(x + 1)
#
# my_func(1)

# 阶乘计算
# def f(x):
#     if x == 1:
#         return 1
#     print()
#     return x * f(x - 1)
# print(f(5))
# list = [4,6,7,9,11,90,44,2]
#
# def sort(list):
#     for i in range(len(list) - 1):
#         for j in range(len(list) - i - 1):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
# sort(list)
# print(list)
#
#
# def find(list, l, r, n):
#     if l >= r:
#         return print(-1)
#
#     mid = (r + l) // 2
#     if list[mid] > n:
#         find(list, l, mid, n)
#     elif list[mid] < n:
#         find(list, mid + 1, r, n)
#     else:
#         return mid
#
# find(list, 0, len(list) - 1,4)

'''
__name__
只有在本模块启动时，__name__变量等于__main__
在什么时候使用
1.可以作为这个模块的入口，在其他语言中，叫做main函数
2.可以作为调试使用
'''
# def my_print():
#     print(__name__)
#
# if __name__ == "__main__":
#     my_print()
#     print(1)
#     print(__name__)

'''
变量的作用域

在python中没有块级的作用域
代码块里的变量，外部是可以调用的
但函数内部的变量，外部不能调用
变量作用域链：就近原则
'''
# if True:
#     name = '1'
# print(name)
#
# def func():
#     name = "2"
# print(name)
#
# name = "3"
# def func():
#     print(name)
# func()

'''
正则表达式：
    元字符：
    .   匹配除换行符以外的任意字符
    \w  匹配字母或数字或下划线或汉字
    \s  匹配任意的空白符
    \d  匹配数字
    \b  匹配单词的开始或结束
    ^   匹配字符串的开始
    $   匹配字符串的结束
    []  匹配[]内的字符
'''
# import re
#
# reg_string = "hello456631python@wa.comhello.@@@xiaoxiao"
# reg = "hello"
# result = re.findall(reg, reg_string)
# print(result)
#
# reg = "^hello"
# result = re.findall(reg, reg_string)
# print(result)
#
# reg = "\w+"
# result = re.findall(reg, reg_string)
# print(result)

'''
反义代码
    \W - 匹配字母或数字或下划线或汉字
    \S - 匹配任意的空白符
    \D - 匹配非数字
    \B - 匹配不是单词的开始或结束
    [^a] - 匹配除了a以外的任意字符
'''
# import re
#
# reg_string = "hella456631python@wa.comhello.@@@xiaoxiao"
# reg = "[ahp456@]"
# result = re.findall(reg, reg_string)
# print(result)

'''
限定符
     *    重复0次或n次
     +    重复1次或n次
     ?    重复0次或1次
    {n}   重复n次
    {n,}  重复n次或者更多次数
    {n,m} 重复n次到m次
'''
# import re
#
# reg_string = "hella456631111python@Wa.Omhello.@@@xiaoxiao"
# reg = "\d{4}"
# result = re.findall(reg, reg_string)
# print(result)
#
# reg = "[A-Za-z0-9]{4}"
# result = re.findall(reg, reg_string)
# print(result)

# ip 练习

import re

# findall 匹配所有
# ip = "this is ip:192.168.1.123 and 172.138.2.15"
# reg = "\d{3}\.\d+\.\d+\.\d+"
# result = re.findall(reg, ip)
# print(result)

# search 只匹配第一个
# ip = "this is ip:192.168.1.123 : 172.138.2.15"
# reg = "(\d{1,3}\.){3}\d{1,3}"
# result = re.search(reg,ip)
# print(result)

'''
组匹配
'''

# s = "this is phone:13888888888 and this is my postcode:012345"
# reg = "this is phone:(\d{11}) and this is my postcode:(\d{6})"
# result = re.search(reg, s).group(0)
# print(result)
# result = re.search(reg, s).group(1)
# print(result)
# result = re.search(reg, s).group(2)
# print(result)

# match 只匹配开头的
# import re
#
# reg_string = "hello456631111python@Wa.Omhello.@@@xiaoxiao"
# reg = "Hello"
# result = re.match(reg, reg_string).group() # 使用re.I
# print(result)

'''
贪婪：尽可能多的匹配
非贪婪：尽可能少的匹配

python默认为贪婪。非贪婪操作符：?
'''

# import re
#
# reg_string = "pythonnnnnnnnnnnnnnnnnpythonHelloPytho"
# reg = "python*?"
# result = re.findall(reg, reg_string)
# print(result)
#
# reg = "python+?"
# result = re.findall(reg, reg_string)
# print(result)
#
# reg = "python??"
# result = re.findall(reg, reg_string)
# print(result)

# lambda
# def make_incrementor(n):
#     return lambda x: x + n
#
#
# f = make_incrementor(42)
# f(0)

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# -*- coding: utf-16 -*-
# print(ord(list('⬁')[0]))

print('1' if 1 // 2 else '0')
