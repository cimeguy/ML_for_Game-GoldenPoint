#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from classEx.class_hw import *
		

# 单元测试
class TestClassFunc(unittest.TestCase):
    # 题目：计算图形面积及周长
    def test_object(self):
        r = Rectangle("rect",2,3)
        t = Triangle("tri",3,4,5)
        c = Circle("c",5)

        self.assertTrue(isinstance(r, Rectangle))
        self.assertTrue(isinstance(t, Triangle))
        self.assertTrue(isinstance(c, Circle))

        self.assertTrue(isinstance(r, Shape))
        self.assertTrue(isinstance(t, Shape))
        self.assertTrue(isinstance(c, Shape))

    def test_calculation(self):
        r = Rectangle("rect",2,3)
        t = Triangle("tri",3,4,5)
        c = Circle("c",5)

        area = r.cal_area()
        per = r.cal_perimeter()
        self.assertEquals(area, 6)
        self.assertEqual(per, 10)

        area = t.cal_area()
        per = t.cal_perimeter()
        self.assertAlmostEqual(area, 6, delta=0.1)
        self.assertEqual(per, 12)

        area = c.cal_area()
        per = c.cal_perimeter()
        self.assertAlmostEqual(area, 78.5, delta=0.1)
        self.assertAlmostEqual(per, 31.4, delta=0.1)

    def test_object_1(self):
        r = Rectangle("rect", 2, 3)
        self.assertTrue(isinstance(r, Rectangle))  # r = Rectangle("rect",2,3)
        self.assertTrue(isinstance(r, Shape))  # r = Rectangle("rect",2,3)

    def test_object_2(self):
        t = Triangle("tri", 3, 4, 5)
        self.assertTrue(isinstance(t, Triangle))  # t = Triangle("tri",3,4,5)
        self.assertTrue(isinstance(t, Shape))  # t = Triangle("tri",3,4,5)

    def test_object_3(self):
        c = Circle("c", 5)
        self.assertTrue(isinstance(c, Circle))  # c = Circle("c",5)
        self.assertTrue(isinstance(c, Shape))  # c = Circle("c",5)

    def test_calculation_1(self):
        r = Rectangle("rect", 2, 3)
        area = r.cal_area()
        self.assertEquals(area, 6)  # r = Rectangle("rect",2,3)  area = r.cal_area()

    def test_calculation_2(self):
        r = Rectangle("rect", 2, 3)
        per = r.cal_perimeter()
        self.assertEqual(per, 10)  # r = Rectangle("rect",2,3)  per = r.cal_perimeter()

    def test_calculation_3(self):
        t = Triangle("tri", 3, 4, 5)
        area = t.cal_area()
        self.assertAlmostEqual(area, 6, delta=0.1)  # t = Triangle("tri",3,4,5)  area = t.cal_area()

    def test_calculation_4(self):
        t = Triangle("tri", 3, 4, 5)
        per = t.cal_perimeter()
        self.assertEqual(per, 12)  # t = Triangle("tri",3,4,5)  per = t.cal_perimeter()

    def test_calculation_5(self):
        c = Circle("c", 5)
        area = c.cal_area()
        self.assertAlmostEqual(area, 78.5, delta=0.1)  # c = Circle("c",5)  area = c.cal_area()

    def test_calculation_6(self):
        c = Circle("c", 5)
        per = c.cal_perimeter()
        self.assertAlmostEqual(per, 31.4, delta=0.1)  # c = Circle("c",5)  per = c.cal_perimeter()

if __name__ == '__main__':
    unittest.main()