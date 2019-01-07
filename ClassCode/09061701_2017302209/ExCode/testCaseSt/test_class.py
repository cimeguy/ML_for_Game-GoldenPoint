#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from forStudent.classEx.class_hw import *
		

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
	

if __name__ == '__main__':
    unittest.main()