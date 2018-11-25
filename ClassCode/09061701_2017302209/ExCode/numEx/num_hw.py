#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目一：二进制与十进制的相互转换
# decimal_int & 0xFFFFFFFF 应该是把负数当作了无符号数处理，返回该负数对应的无符号数的二进制形式
def d2b(decimal_int):
    if isinstance(decimal_int, int):
        b = bin(decimal_int & 0xFFFFFFFF).replace('0b', '')
        return b
    else:
        return "Parameter Error"


def b2d(binary_string, flag = False):
    if isinstance(binary_string, str):
        if len(binary_string) > 32:  # 不能输入超出32位的01序列
            return "Parameter Error"
        for i in binary_string: # 只能是01
            if i not in ['0','1']:
                return "Parameter Error"

        if flag == True and len(binary_string) == 32 and binary_string[0] == '1':  # 负数的情况
            a = int(binary_string, 2)
            b = ((~a) & 0xFFFFFFFF) + 1   # 取反加1
            c= 0-b   # 补充负号
            return c
        else:
            return int(binary_string,2)


# 题目二：类似找零钱的操作
dict = {'item01' : 2.3,  'item02' : 35.8, 'item03' : 16.3, 'item04' : 12,
        'item05' : 13.6, 'item06' : 29,   'item07' : 17.4, 'item08' : 63.9,
        'item09' : 56.7, 'item10' : 23.8}

def list_goods():
    for key in dict:
        print('"' + str(key) + '":' + str(dict[key]) + ',')

shopKeys = dict.keys()
notExist = []
money=[50,20,10,5,1,0.5,0.1]
changes={}

def get_changes(items, pay):
    for item in items:
        if item not in shopKeys:
            notExist.append(item)
    if notExist:
        # 存在不合规商品，输出
        s = '、'.join(notExist) + '不存在，请重新选择。'
        notExist.clear()
        return s
    else:
        # 所有商品合规
        moneySum = 0
        for item in items:
            moneySum += dict[item]
        if moneySum > pay:
            return '支付金额不足，请重新支付。'
        fee = round(float(pay - moneySum),1)
        for k in range(0, 7):
            b = int((fee*10) / (money[k]*10))
            changes[money[k]] = b
            fee = round(fee % money[k],1)
            k = k + 1
        return changes
		

# 题目三：两地之间距离计算
from math import radians, cos, sin, asin, sqrt

# 计算两点p1, p2之间的距离
# p1：（纬度、经度）
# p2: （纬度、经度）
def sphere_distance(p1, p2):
    lat1=p1[0]
    lon1=p1[1]
    lat2=p2[0]
    lon2=p2[1]
    if lat1<0 or lat1 >90 or lat2<0 or lat2 >90 or lon1<0 or lon1>180 or lon2<0 or lon2>180:
        return 'Parameter Error.'
    else:
        # radians python自带的角度转弧度
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return round(c * r,2)
		

# 题目四：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    if not isinstance(number, int):
        return "Parameter Error"
    if number <= 0:
        return "Parameter Error"
    elif number == 1 or number == 2:
        return 1
    else:
        return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)


def fibonacci_loop(number):
    if not isinstance(number, int):
        return "Parameter Error"

    if number <= 0:
        return "Parameter Error"
    elif number == 1 or number == 2:
        return 1
    else:
        f2 = f1 = 1
        for i in range(3, number+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3


if __name__ == '__main__':
    list_goods()                        #测试
    get_changes(['item01'],5)
    get_changes(['item01'],1)
    get_changes(['item01','item11','item13'],100)
	
    dis = sphere_distance((34.24, 108.95), (30.89, 121.33))
    print(dis)
    dis = sphere_distance((34.37069, 107.231507), (34.251739, 108.959))
    print(dis)