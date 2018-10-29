#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numEx.number_hw import *


if __name__ == '__main__':
    list_goods()                        #≤‚ ‘
    get_changes(['item01'],5)
    get_changes(['item01','item01'],5)
    get_changes(['item01','item03'],20)
    get_changes(['item09','item10'],100)
    get_changes(['item15'],1)
    get_changes(['item01'],1)
    get_changes(['item06','item11','item13'],100)