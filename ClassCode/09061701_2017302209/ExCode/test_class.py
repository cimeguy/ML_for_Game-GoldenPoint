#!/usr/bin/python
# -*- coding: UTF-8 -*-
from classEx.class_hw import *
		

# 题目八：计算图形面积及周长
def test_class():
    rect = Rectangle("rect",2,3)
    rect.cal_area()
    rect.cal_perimeter()
    rect.display()
	
    tri = Triangle("tri",3,4,5)
    tri.cal_area()
    tri.cal_perimeter()
    tri.display()
	
    c = Circle("c",5)
    c.cal_area()
    c.cal_perimeter()
    c.display()

	

if __name__ == '__main__':
    test_class()