#!/usr/bin/python
# -*- coding:UTF-8 -*-
import random

# 题目：黄金点游戏的客户端部分

# 字符串，即队伍名称，用于在大屏幕显示，不超过16个字符
def get_player_name():
    name = '我爱Python'
    return name


#  参数 h_data：字典，存放了所有队伍的历史数据。
#  字典包含一个键值，"队伍名称" : "前面每轮提交的数据" 。
#  h_data参数示例：三个玩家，已经玩过四轮，在进行第五轮时，传入的参数h_data。
#  {"我不知道我是谁" : [(12.3,44.5),(33.4,55.6),(22.3,34.5),(33,44)],
#    "super man" : [(42.3,34.5),(23.4,15.6),(72.3,74.5),(93,94)],
#    "帅哥" : [(62.3,47.5),(23.4,57.6),(72.3,24.5),(23,44)]}
#
#  返回值：二元组，即本轮的两个数字，保留三位小数，如(12.618,88.0)。
#  注意控制函数运行时间，过长的运行时间将被判不合格。
#  注意第一次调用时，各位选手存放的历史数据为空列表
def get_number(h_data):
    sum_number = 0
    l = []
    for name, nums in h_data.items():
        if len(nums) > 0:
            n1, n2 = nums[-1]
            sum_number += (n1 + n2)
            l.append(n1)
            l.append(n2)

    g_number = round((0.618 * sum_number/len(h_data)),10)

    if len(l) == 0:
        return random.uniform(10, 99), random.uniform(0, 10)
    else:
        return g_number, random.uniform(g_number, min(2*g_number,99.999))



if __name__ == '__main__':
    history_data = {'Bob': [(12.3, 44.5), (33.4, 55.6), (22.3, 34.5)],
                    'Bart' : [(42.3, 34.5), (23.4, 15.6), (72.3, 74.5)],
                    'Mary' : [(62.3, 47.5), (23.4, 57.6), (72.3, 24.5)]}

    print(get_number(history_data))
    print(get_player_name())

