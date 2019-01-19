#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目八：计算图形面积及周长
class Shape(object):
    def __init__(self,name):
        self.name = name
        self.area = 0
        self.perimeter = 0
		
    def cal_area(self):
        pass
		
    def cal_perimeter(self):
        pass
		
    def display(self):
        print("名称是 " + self.name)
        print("面积是 " + str(self.area))
        print("周长是 " + str(self.perimeter))
		

class Rectangle(Shape):
    def __init__(self, n, a, b):
        super().__init__(n)
        self.a = a
        self.b = b

    def cal_area(self):
        super().cal_area()
        self.area = self.a * self.b
        return self.area

    def cal_perimeter(self):
        super().cal_perimeter()
        self.perimeter = 2 * (self.a + self.b)
        return self.perimeter

class Triangle(Shape):
    def __init__(self, n, a, b, c):
        super(Triangle, self).__init__(n)
        self.a = a
        self.b = b
        self.c = c

    def cal_area(self):
        super().cal_area()
        s = (self.a + self.b + self.c) / 2
        self.area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return self.area

    def cal_perimeter(self):
        super().cal_perimeter()
        self.perimeter = self.a + self.b + self.c
        return self.perimeter


class Circle(Shape):
    def __init__(self, n, a):
        super(Circle, self).__init__(n)
        self.a = a

    def cal_area(self):
        super().cal_area()
        self.area = 3.14 * self.a * self.a
        return self.area

    def cal_perimeter(self):
        super().cal_perimeter()
        self.perimeter = 2 * 3.14 * self.a
        return self.perimeter

if __name__ == '__main__':
    rect = Rectangle("rect", 2, 3)
    rect.cal_area()
    rect.cal_perimeter()
    rect.display()

    tri = Triangle("tri", 3, 4, 5)
    tri.cal_area()
    tri.cal_perimeter()
    tri.display()

    c = Circle("c", 5)
    c.cal_area()
    c.cal_perimeter()
    c.display()