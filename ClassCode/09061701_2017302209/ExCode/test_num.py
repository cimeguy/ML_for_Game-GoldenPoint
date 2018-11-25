#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numEx.num_hw import *


# 题目：类似找零钱的操作
def test_goods():
    list_goods()
    d = get_changes(['item01'],5)
    print(d)
    d = get_changes(['item01','item01'],5)
    print(d)
    d = get_changes(['item01','item03'],20)
    print(d)
    d = get_changes(['item09','item10'],100)
    print(d)
    d = get_changes(['item15'],1)
    print(d)
    d = get_changes(['item01'],1)
    print(d)
    d = get_changes(['item06','item11','item13'],100)
    print(d)


# 题目：二进制与十进制转换器
def test_b2d():
    print(d2b(0))
    print(d2b(12345))
    print(d2b(4294967295))  # 32位的无符号极大值
    print(d2b(-1))
    print(d2b(-12345))
    print(d2b(2147483647))  # 32位的有符号极大值
    print(d2b(-2147483648)) # 32位的有符号极小值
    print(d2b('15ab'))

    print(b2d('0'))
    print(b2d('11000000111001'))
    print(b2d('11111111111111111111111111111111'))
    print(b2d('11111111111111111111111111111111',True))
    print(b2d('11111111111111111100111111000111',True))

    print(b2d('1111111111111111111111111111111'))
    print(b2d('10000000000000000000000000000000'))
    print(b2d('11a11'))



# 计算 Fibonacci 序列的值
# import sys
# sys.setrecursionlimit(2000) # Python中默认最大递归深度为1000，通过setrecursionlimit可设置。
def test_fibonacci():
    print(fibonacci_recursion(0))
    print(fibonacci_loop(0))
    for i in range(1,10):
        print(fibonacci_recursion(i))
        print(fibonacci_loop(i))

    for i in range(30,35):
        print(fibonacci_recursion(i))
        print(fibonacci_loop(i))

# 题目：两地之间距离计算
def test_sphere_distance():
    dis = sphere_distance((34.24, 108.95), (30.89, 121.33))
    print(dis)
	
    dis = sphere_distance((34.37069, 107.231507), (34.251739, 108.959))
    print(dis)	

    dis = sphere_distance((134.37069, 107.231507), (34.251739, 108.959))
    print(dis)
	
    dis = sphere_distance((34.37069, 107.231507), (34.251739, -108.959))
    print(dis)

if __name__ == '__main__':
    #test_goods()
    #test_b2d()
    test_fibonacci()
    #test_sphere_distance()