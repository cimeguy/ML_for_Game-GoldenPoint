#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from numEx.num_hw import *


# 单元测试
class TestNumFunc(unittest.TestCase):
    # 题目：二进制与十进制转换器
    def test_d2b(self):
        self.assertTrue(isinstance(d2b(0), type("")))  # 返回值是否正确
        self.assertEqual(d2b(0), '0')
        self.assertEqual(d2b(12345), '11000000111001')
        self.assertEqual(d2b(4294967295), '11111111111111111111111111111111')  # 32位的无符号极大值
        self.assertEqual(d2b(-1), '11111111111111111111111111111111')

        self.assertEqual(d2b(-12345), '11111111111111111100111111000111')
        self.assertEqual(d2b(2147483647), '1111111111111111111111111111111')   # 32位的有符号极大值
        self.assertEqual(d2b(-2147483648), '10000000000000000000000000000000')   # 32位的有符号极小值

        self.assertEqual(d2b('15ab'), 'Parameter Error.')

    def test_b2d(self):
        self.assertTrue(isinstance(b2d('0'), type(0)))  # 返回值是否正确
        self.assertEqual(b2d('0'), 0)
        self.assertEqual(b2d('11000000111001'), 12345)
        self.assertEqual(b2d('11111111111111111111111111111111'), 4294967295)
        self.assertEqual(b2d('11111111111111111111111111111111',True), -1)

        self.assertEqual(b2d('11111111111111111100111111000111',True), -12345)
        self.assertEqual(b2d('1111111111111111111111111111111'), 2147483647)
        self.assertEqual(b2d('10000000000000000000000000000000'), 2147483648)
        self.assertEqual(b2d('10000000000000000000000000000000',True), -2147483648)

        self.assertEqual(b2d('11a11'), 'Parameter Error.')
        self.assertEqual(b2d(1234), 'Parameter Error.')

    # 题目：类似找零钱的操作
    def test_list_goods(self):
        d = list_goods()
        self.assertTrue(d, type(""))
        self.assertTrue(len(d) > 0)

    def test_get_changes(self):
        d = get_changes(['item01'],5)
        self.assertTrue(isinstance(d,type({})))
        self.assertEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 2, 0.5: 1, 0.1: 2})
        d = get_changes(['item01','item01'],5)
        self.assertEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.5: 0, 0.1: 4})
        d = get_changes(['item01','item03'],20)
        self.assertEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 1, 0.5: 0, 0.1: 4})
        d = get_changes(['item09','item10'],100)
        self.assertEqual(d, {50: 0, 20: 0, 10: 1, 5: 1, 1: 4, 0.5: 1, 0.1: 0})

        d = get_changes(['item15'],1)
        self.assertEqual(d, "item15不存在，请重新选择。")
        d = get_changes(['item01'],1)
        self.assertEqual(d, "支付金额不足，请重新支付。")
        d = get_changes(['item06','item11','item13'],100)
        self.assertEqual(d, "item11、item13不存在，请重新选择。")

    # 计算 Fibonacci 序列的值
    def test_fibonacci(self):
        self.assertEqual(fibonacci_recursion(0), 'Parameter Error.')
        self.assertEqual(fibonacci_recursion(1), 1)
        self.assertEqual(fibonacci_recursion(2), 1)
        self.assertEqual(fibonacci_recursion(3), 2)
        self.assertEqual(fibonacci_recursion(30), 832040)
        self.assertEqual(fibonacci_recursion(34), 5702887)

        self.assertEqual(fibonacci_loop(0), 'Parameter Error.')
        self.assertEqual(fibonacci_loop(1), 1)
        self.assertEqual(fibonacci_loop(2), 1)
        self.assertEqual(fibonacci_loop(3), 2)
        self.assertEqual(fibonacci_loop(30), 832040)
        self.assertEqual(fibonacci_loop(34), 5702887)


    # 题目：两地之间距离计算
    def test_sphere_distance(self):
        dis = sphere_distance((34.24, 108.95), (30.89, 121.33))
        e_dis = abs(dis - 1217.53)
        self.assertTrue(e_dis < 120)  # 10%的计算误差都算对

        dis = sphere_distance((34.37069, 107.231507), (34.251739, 108.959))
        e_dis = abs(dis - 159.21)
        self.assertTrue(e_dis < 15) # 10%的计算误差都算对

        dis = sphere_distance((134.37069, 107.231507), (34.251739, 108.959))
        self.assertEqual(dis, 'Parameter Error.')

        dis = sphere_distance((34.37069, 107.231507), (34.251739, -108.959))
        self.assertEqual(dis, 'Parameter Error.')


if __name__ == '__main__':
    unittest.main()