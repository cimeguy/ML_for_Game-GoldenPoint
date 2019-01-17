#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目八：计算图形面积及周长
class Shape(object):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def cal_area(self):
        if (self.name == 'rect') and len(self.args)==2:
            self.area = round(self.args[0]*self.args[1] , 2)
            return self.area
        elif (self.name == 'tri') and len(self.args)==3:
            self.p = (self.args[0] + self.args[1] + self.args[2]) / 2
            self.s = self.p * (self.p - self.args[0]) * (self.p - self.args[1]) * (self.p - self.args[2])
            self.area = round(self.s ** 0.5, 2)
            return self.area
        elif (self.name == 'c') and len(self.args) == 1:
            self.area = round(self.args[0] ** 2 * 3.14, 2)
            return self.area

    def cal_perimeter(self):
        if (self.name == 'rect') and len(self.args) == 2:
            self.perimeter = round(2*(self.args[0] + self.args[1]), 2)
            return self.perimeter
        elif (self.name == 'tri') and len(self.args) == 3:
            self.perimeter = round(self.args[0] + self.args[1] + self.args[2], 2)
            return self.perimeter
        elif (self.name == 'c') and len(self.args) == 1:
            self.perimeter = round(self.args[0]*2*3.14, 2)
            return self.perimeter

    def display(self):
        return "名称是 %s\n面积是 %s\n周长是 %s" % (self.name, self.area, self.perimeter)


class Rectangle(Shape):
    def __init__(self, name, *args):
        self. name =name
        self.args = args


class Triangle(Shape):
    def __init__(self, name, *args):
        self.name = name
        self.args = args


class Circle(Shape):
    def __init__(self, name, *args):
        self.args = args
        self.name = name


if __name__ == '__main__':
    pass