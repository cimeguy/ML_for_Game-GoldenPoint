#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目一：二进制与十进制的相互转换
# decimal_int & 0xFFFFFFFF 应该是把负数当作了无符号数处理，返回该负数对应的无符号数的二进制形式
def d2b(decimal_int):
    pass


def b2d(binary_string, flag = False):
    pass

# 题目二：类似找零钱的操作
item_dict = {'item01' : 2.3,  'item02' : 35.8, 'item03' : 16.3, 'item04' : 12,
        'item05' : 13.6, 'item06' : 29,   'item07' : 17.4, 'item08' : 63.9,
        'item09' : 56.7, 'item10' : 23.8}

def list_goods():
    pass

shopKeys = item_dict.keys()
notExist = []
money=[50,20,10,5,1,0.5,0.1]
changes={}

def get_changes(items, pay):
    pass
		

# 题目三：两地之间距离计算

# 计算两点p1, p2之间的距离
# p1：（纬度、经度）
# p2: （纬度、经度）
def sphere_distance(p1, p2):
    pass
		

# 题目四：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    pass


def fibonacci_loop(number):
    pass


if __name__ == '__main__':
    pass
