#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目一：二进制与十进制的相互转换
def d2b(decimal_int):
    if type(decimal_int)!=type(0):
        return 'Parameter Error.'
    if decimal_int < -(2**32) or decimal_int > 2**32-1:
        return 'Parameter Error.'
    else:
        bi=''
        if decimal_int==0:
            return '0'
        elif decimal_int>0:
            while decimal_int>0:
                n=decimal_int%2
                if n==1:
                    bi+='1'
                else:
                    bi+='0'
                decimal_int=decimal_int//2
            bi=bi[::-1]

        else:
            decimal_int=-decimal_int
            while decimal_int>0:
                n=decimal_int%2
                if n==1:
                    bi+='1'
                else:
                    bi+='0'
                decimal_int=decimal_int//2
            bi=bi[::-1]
            ling='0'*(32-len(bi))
            bi=ling+bi
            bi=bi.replace('1','2')
            bi=bi.replace('0','1')
            bi=bi.replace('2','0')
            for num in range(1,len(bi)+1):
                if bi[-num]=='0':
                    list_bin=list(bi)
                    list_bin[-num]='1'
                    bi=''.join(list_bin)
                    for num2 in range(1,num):
                        bi=bi.replace(bi[-num2],'0')
                    break

            return bi

        return bi


def b2d(binary_string, flag = False):
    if type(binary_string)!=type(''):
        return 'Parameter Error.'
    for s in binary_string:
        if s!='1' and s!='0':
            return 'Parameter Error.'

    if flag == False:
        dec = 0
        for num in range(0, len(binary_string)):
            if binary_string[num] == str(1):
                dec += 2 ** (len(binary_string) - num - 1)
    else:
        if binary_string[0]==0:
            dec = 0
            for num in range(0, len(binary_string)):
                if binary_string[num] == str(1):
                    dec += 2 ** (len(binary_string) - num - 1)
        else:
            binary_string=binary_string[1:]
            binary_string=int(binary_string)

            binary_string-=1
            binary_string=str(binary_string)

            binary_string=binary_string.replace('0','2')
            binary_string =binary_string.replace('1','0')

            binary_string =binary_string.replace('2','1')
            dec = 0
            for num in range(0, len(binary_string)):
                if binary_string[num] == str(1):
                    dec += 2 ** (len(binary_string) - num - 1)
            dec=-dec
    return dec


# 题目二：类似找零钱的操作
money=[50,20,10,5,1,0.5,0.1]  # 纸币面额
item_dict = {'item01' : 2.3,  'item02' : 35.8, 'item03' : 16.3, 'item04' : 12,
        'item05' : 13.6, 'item06' : 29,   'item07' : 17.4, 'item08' : 63.9,
        'item09' : 56.7, 'item10' : 23.8}  # 商品名称与价格


def list_goods():
    return '''{'item01': 2.3, 'item02': 35.8, 'item03': 16.3, 'item04': 12, 'item05': 13.6, 'item06': 29, 'item07':
                    17.4, 'item08': 63.9, 'item09': 56.7, 'item10': 23.8}'''


def get_changes(items, pay):
    canpay = True
    items_not = []
    for item in items:
        if item not in item_dict:
            items_not.append(item)
            canpay = False
    if not canpay:
        if len(items_not) == 1:
            return items_not[0] + '不存在，请重新选择。'
        elif len(items_not) == 2:
            return items_not[0] + '、' + items_not[1] + '不存在，请重新选择。'
        else:
            inexist = ''
            for number in range(len(items_not) - 1):
                inexist += items_not[number] + '、'
            inexist += items_not[-1]
            return inexist + '不存在，请重新选择。'
    else:
        price = 0
        for item in items:
            price += item_dict[item]
        if pay < price:
            return '支付金额不足，请重新支付。'
        else:
            change = pay - price
            changelist = {50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.5: 0, 0.1: 0}
            for mianzhi in money:
                while change >= mianzhi:
                    changelist[mianzhi] = int(change // mianzhi)
                    change = change - mianzhi * (change // mianzhi)
            return changelist
		

# 题目三：两地之间距离计算
# 计算两点p1, p2之间的距离
# p1：二元组，（纬度、经度）
# p2: 二元组，（纬度、经度）
from math import radians, cos, sin, asin, sqrt
p1=()
p2=()
def sphere_distance(p1, p2):
    lat_1 = p1[0]
    lon_1 = p1[1]
    lat_2 = p2[0]
    lon_2 = p2[1]
    if lat_1 < 0 or lat_1 > 90 or lat_2 < 0 or lat_2 > 90 or lon_1 < 0 or lon_1 > 180 or lon_2 < 0 or lon_2 > 180:
        return 'Parameter Error.'
    else:

        lat_1, lon_1, lat_2, lon_2 = map(radians, [lat_1, lon_1, lat_2, lon_2])

        # haversine公式
        dlon = lon_2 - lon_1
        dlat = lat_2 - lat_1
        a = sin(dlat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return round(c * r,2)
		

# 题目四：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    if number <= 0:
        return 'Parameter Error.'
    elif number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        return fibonacci_loop(number - 1) + fibonacci_loop(number - 2)


def fibonacci_loop(number):
    Fibonacci = list(range(number + 2))
    Fibonacci[0] = 1
    Fibonacci[1] = 1
    if number <= 0:
        return 'Parameter Error.'
    else:
        for num in range(number):
            if num >= 2:
                Fibonacci[num] = Fibonacci[num - 1] + Fibonacci[num - 2]
        return Fibonacci[number - 1]


if __name__ == '__main__':
    print(sphere_distance((34.24, 108.95), (30.89, 121.33)))
