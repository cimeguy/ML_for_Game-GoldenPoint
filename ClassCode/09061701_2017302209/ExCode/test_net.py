#!/usr/bin/python
# -*- coding: UTF-8 -*-
from netEx.net_hw import *


def test_net():
   # print(get_support_city(""))
   citys = get_support_city("陕西")
   name = "西安"
   if name in citys:
       print(get_weather(name))
       # get_weather(citys[name])
	

if __name__ == '__main__':
    test_net()
