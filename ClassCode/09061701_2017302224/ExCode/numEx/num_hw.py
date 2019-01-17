#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目一：二进制与十进制的相互转换
INT32_MAX = 2147483647
INT32_MIN = -2147483648


class ParameterError(Exception):
    pass


def d2b(decimal_int):
    typ = type(decimal_int)
    if'int'in'%s' % typ:
        if INT32_MIN <= decimal_int & decimal_int <= INT32_MAX:
            stri = str(decimal_int)
            if (stri[0] != '-') & (stri[0] != '0'):
                def result(decimal_int):
                    res = ''

                    if decimal_int:
                        res = result(decimal_int // 2)
                        return res + str(decimal_int % 2)
                    else:
                        return res
            elif decimal_int == 0:
                return str(decimal_int)
            else:
                def min(minus):
                    res = ''

                    if minus:
                        res = min(minus // 2)
                        return res + str(minus % 2)
                    else:
                        return res

                all = 11111111111111111111111111111111
                minus = int(stri.strip('-'))
                m = all - int(min(minus)) + 1
                return str(m)

            r = result(decimal_int)
            return str(r)
    else:
        return 'Parameter Error.'


def b2d(binary_string, flag=False):
    try:
        length = len(binary_string)
        if flag != 1:
            try:
                res = int(binary_string,2)
                return res
            except:
                return 'Parameter Error.'
        elif flag:
            if length == 32:
                try:
                    all = 11111111111111111111111111111111
                    bina = int(binary_string) - 1
                    bina1 = all - bina
                    res = int(str(bina1), 2)
                    return 0-res
                except:
                    return 'Parameter Error.'
    except:
        return 'Parameter Error.'


# 题目二：类似找零钱的操作
from collections import OrderedDict
money = [50, 20, 10, 5, 1, 0.5, 0.1]  # 纸币面额
item_dict = {'item01': 2.3,  'item02': 35.8, 'item03': 16.3, 'item04': 12,
        'item05': 13.6, 'item06': 29,   'item07': 17.4, 'item08': 63.9,
        'item09': 56.7, 'item10': 23.8}  # 商品名称与价格


def list_goods():

    dic = OrderedDict(item_dict)
    dic = dict(dic)
    return dic


def get_changes(items, pay):
    d = list_goods()
    nogoods = ''
    for item in items:
        if item not in d:
            nogoods = nogoods+item+'、'
    if nogoods:
        nogoods = nogoods.rstrip('、')
        return "%s不存在，请重新选择。"%str(nogoods)
    price = 0
    price+=d[item]
    if ( price > pay ) :
        return "支付金额不足，请重新支付。"
    else:
        price = pay-price
        c50 = 0
        c20 = 0
        c10 = 0
        c5 = 0
        c1 = 0
        c05 = 0
        c01 = 0
        d = {50: c50, 20: c20, 10: c10, 5: c5, 1: c1, 0.5: c05, 0.1: c01}
        while price >= 50:
            price -= 50
            c50 +=1
            d[50] = c50
            if price == 0:
                return d
        while price >= 20:
            price -= 20
            c20 += 1
            d[20] = c20
            if price == 0:
                return d
        while price >= 10:
            price -= 10
            c10 += 1
            d[10] = c10
            if price == 0:
                return d
        while price >= 5:
            price -= 5
            c5 += 1
            d[5] = c5
            if price == 0:
                return d
        while price >= 1:
            price -= 1
            c1 += 1
            d[1] = c1
            price = round(price,4)
            if price == 0:
                return d
        while price >= 0.5:
            price -= 0.5
            c05 += 1
            d[0.5] = c05
            price = round(price, 4)
            if price == 0:
                return d
        while price >= 0.1:
            price -= 0.1
            c01 += 1
            d[0.1] = c01
            price = round(price, 4)
            if price == 0:
                return d


# 题目三：两地之间距离计算
# 计算两点p1, p2之间的距离
# p1：二元组，（纬度、经度）
# p2: 二元组，（纬度、经度）

def sphere_distance(p1,p2):
    from math import radians, cos, sin, asin, sqrt
    r = 6371
    if (p1[0] >=0 and p1[0] <=90) and (p2[0] >=0 and p2[0] <=90) and (p1[1] >=0 and p1[1] <=180) and (p2[1] >=0 and p2[1] <=180):
        p1[0], p1[1], p2[0], p2[1] = map(radians, [p1[0], p1[1], p2[0], p2[1]])
        weiducha = p2[0] - p1[0]
        jinducha = p2[1] - p1[1]
        distance = 2*asin(sqrt(sin(weiducha/2)**2+cos(p1[0])*cos(p2[0])*sin(jinducha/2)**2))*r
        distance = round(distance, 2)
        return distance
    else:
        return 'Parameter Error.'


# 题目四：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    typ = type(number)
    if ('int' in str(typ)) and number >0:
        if number == 2:
            return 1
        elif number<2:
            return  number
        return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)
    else:
        return 'Parameter Error.'


def fibonacci_loop(number):
    n1 = 0
    n2 = 1
    typ = type(number)
    n=1
    if ('int' in str(typ)) and number > 0:
        for count in range(1, number):
                n = n2 + n1
                n1 = n2
                n2 = n
        return n
    else:
        return 'Parameter Error.'


if __name__ == '__main__':
    pass
