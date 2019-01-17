#!/usr/bin/python
# -*- coding:UTF-8 -*-


# 题目：黄金点游戏的客户端部分

def get_player_name():
    name = '我爱Python'
    return name


#  参数 h_data：列表，存放了所有队伍的历史数据。
#  列表元素为字典形式，字典包含两个键值，name表示队伍名称，numbers表示前面每轮提交的数据。
#  history_data参数示例：三个玩家，已经玩过四轮，在进行第五轮时，传入的参数history_data。
#  [ {"name" : "我不知道我是谁", "numbers" : [(12.3,44.5),(33.4,55.6),(22.3,34.5),(33,44)]},
#    {"name" : "super man", "numbers" : [(42.3,34.5),(23.4,15.6),(72.3,74.5),(93,94)]},
#    {"name" : "帅哥", "numbers" : [(62.3,47.5),(23.4,57.6),(72.3,24.5),(23,44)]} ]
#
#  返回值：二元组，即本轮的两个数字，保留三位小数，如(12.618,88.0)。
#  注意控制函数运行时间，过长的运行时间将被判不合格。
def get_number(h_data):
    number = []
    for i in range(0, len(h_data)):
        number.append(h_data[i]['numbers'])
    sum_number = 0
    for j in range(0, len(number)):
        sum_number += number[j][0][0] + number[j][0][1]
    G = sum_number/6 * 0.618
    data1 = G
    data2 = G + 1
    tup = (data1, data2)
    return tup


if __name__ == '__main__':
    history_data = [{'name': 'Bob', 'numbers': [(12.3, 44.5), (33.4, 55.6), (22.3, 34.5)]},
                    {'name': 'Bart', 'numbers': [(42.3, 34.5), (23.4, 15.6), (72.3, 74.5)]},
                    {'name': 'Mary', 'numbers': [(62.3, 47.5), (23.4, 57.6), (72.3, 24.5)]}]

    print(get_number(history_data))
    print(get_player_name())

