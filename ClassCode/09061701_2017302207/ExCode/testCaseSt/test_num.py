#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
# 注意发布到码云时，需要去掉forStudent前缀
from numEx.num_hw import *
from numEx.golden_hw import *


# 单元测试
class TestNumFunc(unittest.TestCase):
    # 题目：二进制与十进制转换器
    def test_d2b(self):
        self.assertTrue(isinstance(d2b(0), type("")))  # 返回值是否正确
        self.assertEqual(d2b(0), '0')
        self.assertEqual(d2b(12345), '11000000111001')
        self.assertEqual(d2b(-12345), '11111111111111111100111111000111')
        self.assertEqual(d2b('15ab'), 'Parameter Error.')
        self.assertEqual(d2b(4294967295), '11111111111111111111111111111111')  # 32位的无符号极大值

        self.assertEqual(d2b(-1), '11111111111111111111111111111111')
        self.assertEqual(d2b(2147483647), '1111111111111111111111111111111')  # 32位的有符号极大值
        self.assertEqual(d2b(-2147483648), '10000000000000000000000000000000')  # 32位的有符号极小值
        self.assertEqual(d2b('15ab'), 'Parameter Error.')
    def test_b2d(self):
        self.assertTrue(isinstance(b2d('0'), type(0)))  # 返回值是否正确
        self.assertEqual(b2d('0'), 0)
        self.assertEqual(b2d('11000000111001'), 12345)
        self.assertEqual(b2d('11111111111111111100111111000111',True), -12345)
        self.assertEqual(b2d('11a11'), 'Parameter Error.')
        self.assertEqual(b2d(1234), 'Parameter Error.')

        self.assertTrue(isinstance(b2d('0'), type(0)))  # 返回值是否正确

        self.assertEqual(b2d('0'), 0)

        self.assertEqual(b2d('11000000111001'), 12345)

        self.assertEqual(b2d('11111111111111111111111111111111'), 4294967295)

        self.assertEqual(b2d('11111111111111111111111111111111', True), -1)

        self.assertEqual(b2d('11111111111111111100111111000111', True), -12345)


        self.assertEqual(b2d('1111111111111111111111111111111'), 2147483647)


        self.assertEqual(b2d('10000000000000000000000000000000'), 2147483648)

    def test_b2d_9(self):
        self.assertEqual(b2d('10000000000000000000000000000000', True), -2147483648)


        self.assertEqual(b2d('11a11'), 'Parameter Error.')


        self.assertEqual(b2d(1234), 'Parameter Error.')

    def test_d2b_8(self):
        self.assertEqual(d2b(-2147483648), '10000000000000000000000000000000')  # 32位的有符号极小值
    # 题目：类似找零钱的操作
    def test_list_goods(self):
        d = list_goods()
        self.assertTrue(d, type(""))
        self.assertTrue(len(d) > 0)

    def test_get_changes(self):
        d = get_changes(['item01'],5)
        self.assertTrue(isinstance(d,type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 2, 0.5: 1, 0.1: 2})
        d = get_changes(['item01','item01'],5)
        self.assertTrue(isinstance(d,type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.5: 0, 0.1: 4})
        d = get_changes(['item15'],1)
        self.assertEqual(d, "item15不存在，请重新选择。")
        d = get_changes(['item01'],1)
        self.assertEqual(d, "支付金额不足，请重新支付。")
        d = get_changes(['item06','item11','item13'],100)
        self.assertEqual(d, "item11、item13不存在，请重新选择。")

    def test_get_changes_3(self):
        d = get_changes(['item01', 'item03'], 20)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 1, 0.5: 0, 0.1: 4})

    def test_list_goods_1(self):
        d = list_goods()
        self.assertTrue(d, type(""))

    def test_list_goods_2(self):
        d = list_goods()
        self.assertTrue(d, type(""))
        self.assertTrue(len(d) > 0)

    def test_get_changes_1(self):
        d = get_changes(['item01'], 5)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 2, 0.5: 1, 0.1: 2})

    def test_get_changes_2(self):
        d = get_changes(['item01', 'item01'], 5)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.5: 0, 0.1: 4})

    def test_get_changes_3(self):
        d = get_changes(['item01', 'item03'], 20)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 1, 0.5: 0, 0.1: 4})

    def test_get_changes_4(self):
        d = get_changes(['item09', 'item10'], 100)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 1, 5: 1, 1: 4, 0.5: 1, 0.1: 0})

    def test_get_changes_5(self):
        d = get_changes(['item15'], 1)
        self.assertEqual(d, "item15不存在，请重新选择。")

    def test_get_changes_6(self):
        d = get_changes(['item01'], 1)
        self.assertEqual(d, "支付金额不足，请重新支付。")

    def test_get_changes_7(self):
        d = get_changes(['item06', 'item11', 'item13'], 100)
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

    def test_d2b_1(self):
        self.assertTrue(isinstance(d2b(0), type("")))  # 返回值是否正确

    def test_d2b_2(self):
        self.assertEqual(d2b(0), '0')

    def test_d2b_3(self):
        self.assertEqual(d2b(12345), '11000000111001')

    def test_d2b_4(self):
        self.assertEqual(d2b(4294967295), '11111111111111111111111111111111')  # 32位的无符号极大值

    def test_d2b_5(self):
        self.assertEqual(d2b(-1), '11111111111111111111111111111111')

    def test_d2b_6(self):
        self.assertEqual(d2b(-12345), '11111111111111111100111111000111')

    def test_d2b_7(self):
        self.assertEqual(d2b(2147483647), '1111111111111111111111111111111')  # 32位的有符号极大值

    def test_d2b_8(self):
        self.assertEqual(d2b(-2147483648), '10000000000000000000000000000000')  # 32位的有符号极小值

    def test_d2b_9(self):
        self.assertEqual(d2b('15ab'), 'Parameter Error.')

    def test_b2d_1(self):
        self.assertTrue(isinstance(b2d('0'), type(0)))  # 返回值是否正确

    def test_b2d_2(self):
        self.assertEqual(b2d('0'), 0)

    def test_b2d_3(self):
        self.assertEqual(b2d('11000000111001'), 12345)

    def test_b2d_4(self):
        self.assertEqual(b2d('11111111111111111111111111111111'), 4294967295)

    def test_b2d_5(self):
        self.assertEqual(b2d('11111111111111111111111111111111', True), -1)

    def test_b2d_6(self):
        self.assertEqual(b2d('11111111111111111100111111000111', True), -12345)

    def test_b2d_7(self):
        self.assertEqual(b2d('1111111111111111111111111111111'), 2147483647)

    def test_b2d_8(self):
        self.assertEqual(b2d('10000000000000000000000000000000'), 2147483648)

    def test_b2d_9(self):
        self.assertEqual(b2d('10000000000000000000000000000000', True), -2147483648)

    def test_b2d_10(self):
        self.assertEqual(b2d('11a11'), 'Parameter Error.')

    def test_b2d_11(self):
        self.assertEqual(b2d(1234), 'Parameter Error.')

    # 题目：类似找零钱的操作
    def test_list_goods_1(self):
        d = list_goods()
        self.assertTrue(d, type(""))

    def test_list_goods_2(self):
        d = list_goods()
        self.assertTrue(d, type(""))
        self.assertTrue(len(d) > 0)

    def test_get_changes_1(self):
        d = get_changes(['item01'], 5)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 2, 0.5: 1, 0.1: 2})

    def test_get_changes_2(self):
        d = get_changes(['item01', 'item01'], 5)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.5: 0, 0.1: 4})

    def test_get_changes_3(self):
        d = get_changes(['item01', 'item03'], 20)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 0, 5: 0, 1: 1, 0.5: 0, 0.1: 4})

    def test_get_changes_4(self):
        d = get_changes(['item09', 'item10'], 100)
        self.assertTrue(isinstance(d, type({})))
        self.assertDictEqual(d, {50: 0, 20: 0, 10: 1, 5: 1, 1: 4, 0.5: 1, 0.1: 0})

    def test_get_changes_5(self):
        d = get_changes(['item15'], 1)
        self.assertEqual(d, "item15不存在，请重新选择。")

    def test_get_changes_6(self):
        d = get_changes(['item01'], 1)
        self.assertEqual(d, "支付金额不足，请重新支付。")

    def test_get_changes_7(self):
        d = get_changes(['item06', 'item11', 'item13'], 100)
        self.assertEqual(d, "item11、item13不存在，请重新选择。")

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_recursion(0), 'Parameter Error.')

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_recursion(1), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_recursion(2), 1)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci_recursion(3), 2)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci_recursion(30), 832040)

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci_recursion(34), 5702887)

    def test_fibonacci_7(self):
        self.assertEqual(fibonacci_loop(0), 'Parameter Error.')

    def test_fibonacci_8(self):
        self.assertEqual(fibonacci_loop(1), 1)

    def test_fibonacci_9(self):
        self.assertEqual(fibonacci_loop(2), 1)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci_loop(3), 2)

    def test_fibonacci_11(self):
        self.assertEqual(fibonacci_loop(30), 832040)

    def test_fibonacci_12(self):
        self.assertEqual(fibonacci_loop(34), 5702887)

    def test_sphere_distance_1(self):
        dis = sphere_distance((34.24, 108.95), (30.89, 121.33))
        self.assertAlmostEqual(dis, 1217.53, delta=100)

    def test_sphere_distance_2(self):
        dis = sphere_distance((34.37069, 107.231507), (34.251739, 108.959))
        self.assertAlmostEqual(dis, 159.21, delta=10)

    def test_sphere_distance_3(self):
        dis = sphere_distance((134.37069, 107.231507), (34.251739, 108.959))
        self.assertEqual(dis, 'Parameter Error.')

    def test_sphere_distance_4(self):
        dis = sphere_distance((34.37069, 107.231507), (34.251739, -108.959))
        self.assertEqual(dis, 'Parameter Error.')

    # 题目：黄金点客户端测试
    def test_golden_number(self):
        self.assertTrue(isinstance(get_player_name(), type("")))  # 返回值类型是否正确
        self.assertGreater(len(get_player_name()), 0)

        h = {'Bob': [], 'Bart' : [], 'Mary' : []}
        num = get_number(h)
        self.assertTrue(isinstance(num, type((1,2))))  # 返回值类型是否正确
        self.assertEqual(len(num), 2)
        self.assertGreater(num[0], 0)
        self.assertGreater(num[1], 0)
        self.assertLess(num[0], 100)
        self.assertLess(num[1], 100)

        h = {'Bob': [(12.3, 44.5)], 'Bart' : [(42.3, 34.5)], 'Mary' : [(62.3, 47.5)]}
        num = get_number(h)
        self.assertTrue(isinstance(num, type((1,2))))  # 返回值类型是否正确
        self.assertEqual(len(num), 2)
        self.assertGreater(num[0], 0)
        self.assertGreater(num[1], 0)
        self.assertLess(num[0], 100)
        self.assertLess(num[1], 100)

        h = {'Bob': [(12.3, 44.5), (33.4, 55.6)],
                'Bart' : [(42.3, 34.5), (23.4, 15.6)],
                'Mary' : [(62.3, 47.5), (23.4, 57.6)]}
        num = get_number(h)
        self.assertTrue(isinstance(num, type((1,2))))  # 返回值类型是否正确
        self.assertEqual(len(num), 2)
        self.assertGreater(num[0], 0)
        self.assertGreater(num[1], 0)
        self.assertLess(num[0], 100)
        self.assertLess(num[1], 100)

        h = {'Bob': [(12.3, 44.5), (33.4, 55.6), (22.3, 34.5)],
                'Bart' : [(42.3, 34.5), (23.4, 15.6), (72.3, 74.5)],
                'Mary' : [(62.3, 47.5), (23.4, 57.6), (72.3, 24.5)]}
        num = get_number(h)
        self.assertTrue(isinstance(num, type((1,2))))  # 返回值类型是否正确
        self.assertEqual(len(num), 2)
        self.assertGreater(num[0], 0)
        self.assertGreater(num[1], 0)
        self.assertLess(num[0], 100)
        self.assertLess(num[1], 100)


if __name__ == '__main__':
    unittest.main()
