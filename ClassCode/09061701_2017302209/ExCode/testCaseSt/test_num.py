#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from forStudent.numEx.num_hw import *
from forStudent.numEx.golden_hw import *

# 单元测试
class TestNumFunc(unittest.TestCase):
    # 题目：二进制与十进制转换器
    def test_d2b(self):
        self.assertTrue(isinstance(d2b(0), type("")))  # 返回值是否正确
        self.assertEqual(d2b(0), '0')
        self.assertEqual(d2b(12345), '11000000111001')
        self.assertEqual(d2b(-12345), '11111111111111111100111111000111')
        self.assertEqual(d2b('15ab'), 'Parameter Error.')

    def test_b2d(self):
        self.assertTrue(isinstance(b2d('0'), type(0)))  # 返回值是否正确
        self.assertEqual(b2d('0'), 0)
        self.assertEqual(b2d('11000000111001'), 12345)
        self.assertEqual(b2d('11111111111111111100111111000111',True), -12345)
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
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 2, 0.5: 1, 0.1: 2})
        d = get_changes(['item15'],1)
        self.assertEqual(d, "item15不存在，请重新选择。")
        d = get_changes(['item01'],1)
        self.assertEqual(d, "支付金额不足，请重新支付。")
        d = get_changes(['item06','item11','item13'],100)
        self.assertEqual(d, "item11、item13不存在，请重新选择。")


    # 计算 Fibonacci 序列的值
    def test_fibonacci(self):
        self.assertEqual(fibonacci_recursion(0), 'Parameter Error.')
        self.assertEqual(fibonacci_recursion(3), 2)
        self.assertEqual(fibonacci_recursion(30), 832040)

        self.assertEqual(fibonacci_loop(0), 'Parameter Error.')
        self.assertEqual(fibonacci_loop(3), 2)
        self.assertEqual(fibonacci_loop(30), 832040)


    # 题目：两地之间距离计算
    def test_sphere_distance(self):
        dis = sphere_distance((34.24, 108.95), (30.89, 121.33))
        self.assertAlmostEqual(dis, 1217.53, delta=100)

        dis = sphere_distance((134.37069, 107.231507), (34.251739, 108.959))
        self.assertEqual(dis, 'Parameter Error.')


    # 题目：黄金点客户端测试
    def test_golden_number(self):
        self.assertTrue(isinstance(get_player_name(), type("")))  # 返回值类型是否正确
        self.assertGreater(len(get_player_name()), 0)

        h = [ {"name":"我不知道我是谁", "numbers":[(12.3,44.5),(33.4,55.6),(22.3,34.5),(33,44)]},
            {"name":"super man", "numbers":[(42.3,34.5),(23.4,15.6),(72.3,74.5),(93,94)]}]

        num = get_number(h)
        self.assertTrue(isinstance(num, type((1,2))))  # 返回值类型是否正确
        self.assertEqual(len(num), 2)

        self.assertGreater(num[0], 0)
        self.assertGreater(num[1], 0)

        self.assertLess(num[0], 100)
        self.assertLess(num[1], 100)


if __name__ == '__main__':
    unittest.main()