#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numEx.num_hw import *
from numEx.num_hw01 import *


# 类似找零钱的操作
def test_goods():
    list_goods()             
    get_changes(['item01'],5)
    get_changes(['item01','item01'],5)
    get_changes(['item01','item03'],20)
    get_changes(['item09','item10'],100)
    get_changes(['item15'],1)
    get_changes(['item01'],1)
    get_changes(['item06','item11','item13'],100)
	
	
# 二进制与十进制转换器
def test_b2d():
    print(d2b(15))
    print(d2b(12345))
    print(d2b(-1))
    print(b2d('1111'))
    print(b2d('101111'))
    print(d2b('15ab'))
	

# 计算 Fibonacci 序列的值
def test_fibonacci():
    fibonacci_recursion(0)
    fibonacci_loop(0)
    for i in range(1,10):
        print(fibonacci_recursion(10))
        print(" ")
        print(fibonacci_loop(10))
	

if __name__ == '__main__':
    #test_goods()
    #test_b2d()
    test_fibonacci()