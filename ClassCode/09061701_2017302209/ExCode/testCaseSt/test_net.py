#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from forStudent.netEx.net_hw import *


# 单元测试
class TestNumFunc(unittest.TestCase):
    # 题目：获取当前天气情况
    def test_net(self):
       citys = get_support_city("陕西")
       self.assertIn('西安',citys.keys())

       name = "西安"
       self.assertGreater(len(get_weather(name)), 0)


if __name__ == '__main__':
    unittest.main()
