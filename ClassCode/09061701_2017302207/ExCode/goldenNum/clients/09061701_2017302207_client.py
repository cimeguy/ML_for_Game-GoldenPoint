#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# 题目：黄金点游戏的客户端部分

# 字符串，即队伍名称，用于在大屏幕显示，不超过16个字符。
def get_player_name():
    name = 'GaoLi'
    return name


#  参数 h_data：字典，存放了所有队伍的历史数据。
#  字典包含一个键值，"队伍名称" : "前面每轮提交的数据" 。
#  h_data参数示例：三个玩家，已经玩过四轮，在进行第五轮时，传入的参数h_data。
#  传入的参数示例：h_data = {'Bob': [(12.3, 44.5), (33.4, 55.6), (22.3, 34.5)],
#                    'Bart' : [(42.3, 34.5), (23.4, 15.6), (72.3, 74.5)],
#                    'Mary' : [(62.3, 47.5), (23.4, 57.6), (72.3, 24.5)]}
#
#  返回值：二元组，即本轮的两个数字，如(12.618,88.0)，两个数字均应大于0，小于100。
#  注意控制函数运行时间，过长的运行时间将被判不合格。
#  注意第一次调用时，各位选手存放的历史数据为空列表
def get_number(h_data):
    sum_number = 0
    generation = []
    g_group = []
    det_group = []
    # for name, nums in h_data.items():
    #     if len(nums) > 0:
    #         n1, n2 = nums[-1]
    #
    #         sum_number += (n1 + n2)

    # g_number = round((0.618 * sum_number/len(h_data)),10)

    for name, nums in h_data.items():
        if len(nums) == 0:
            g_number = 50
            data1 = g_number % 100
            data2 = (g_number + 1) % 100
            tup = (data1 + 0.0000000001, data2)
            return tup
        else:

            # n_list = [[] for row in range(len(h_data[name]))]
            #  col列(玩家数) row 行（轮数）

            for num_generation in range(len(h_data[name])):
                sum_number = 0
                # det_sum = 0
                # n_list[num_generation].append(num_generation+1)
                generation.append(num_generation + 1)  # 每一轮
                for name_gen, nums2 in h_data.items():
                    if len(nums) > 0:
                        n1, n2 = nums2[num_generation]
                        n = n1 + n2
                        sum_number += n
                        # det_sum += (n1-n2)
                        # n_list[num_generation].append(n)
                g_number = round((0.618 * sum_number / len(h_data)), 10)

                g_group.append(g_number)
                # det_data = round(( det_sum/ len(h_data)), 10)
                # det_group.append(det_data)
            g_before = [50] + g_group[:-1]

            # if (len(n_list)) == 1:
            #     n_new = [0,100,100,100]
            # else:
            #     n_new = n_list[-2]
            # poly = PolynomialFeatures(degree=2)
            # N = poly.fit_transform(n_new)
            # newlist = np.array(n_list[-1]).reshape(len(n_list[-1],-1))

            g_group = np.array(g_group).reshape([len(g_group), -1])
            generation = np.array(generation).reshape([len(generation), -1])
            g_before = np.array(g_before).reshape([len(g_before), -1])
            poly = PolynomialFeatures(degree=2)
            # generation_poly =poly.fit_transform(generation)
            g_before_poly = poly.fit_transform(g_before)
            # det_group = np.array(det_group).reshape([len(det_group),-1])
            for name, nums in h_data.items():
                gen = len(h_data[name])
                break
            # gen = len(n_list)

            next = np.array([g_before[-1]]).reshape(1, -1)
            next_poly = poly.fit_transform(next)
            line = LinearRegression()
            # # ridge.fit(generation,g_group)
            line.fit(g_before_poly, g_group)
            g_next = line.predict(next_poly)
            # # # ridge2 = Ridge()
            # # # ridge2.fit(generation,det_group)
            # # # det_next = ridge2.predict(np.array([gen+1]).reshape(1,-1))
            g_next_ = g_next[0][0] % 100
            # # det_next_ = det_next[0][0]
            # # data1_next = round(g_next_ +det_next_/2,10)
            # # data2_next = round(g_next_ - det_next_/2,10)

            return g_number, g_next_


# 可用于代码运行时间的简单测试
def get_time():
    start = time.clock()
    get_number(history_data)
    end = time.clock()
    pass_time = ("%.10f" % (end - start))
    return pass_time


if __name__ == '__main__':
    print(get_player_name())

    history_data = {'Bob': [], 'Bart' : [], 'Mary' : []}
    print(get_number(history_data))

    history_data = {'Bob': [(12.3, 44.5)], 'Bart' : [(42.3, 34.5)], 'Mary' : [(62.3, 47.5)]}
    print(get_number(history_data))

    history_data = {'Bob': [(12.3, 44.5), (33.4, 55.6)],
            'Bart' : [(42.3, 34.5), (23.4, 15.6)],
            'Mary' : [(62.3, 47.5), (23.4, 57.6)]}
    print(get_number(history_data))

    history_data = {'Bob': [(12.3, 44.5), (33.4, 55.6), (22.3, 34.5)],
            'Bart' : [(42.3, 34.5), (23.4, 15.6), (72.3, 74.5)],
            'Mary' : [(62.3, 47.5), (23.4, 57.6), (72.3, 24.5)]}
    print(get_number(history_data))

