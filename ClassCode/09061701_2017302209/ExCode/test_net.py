#!/usr/bin/python
# -*- coding: UTF-8 -*-
from netEx.net_hw import *


def test_net():
    res = get_weather('北京')
    print(res)
	

if __name__ == '__main__':
    test_net()
