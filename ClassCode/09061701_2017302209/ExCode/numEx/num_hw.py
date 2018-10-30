#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
        print('、'.join(notExist) + '不存在，请重新选择。')
        notExist.clear()
        return
    else:
        # 所有商品合规
        moneySum = 0
        for item in items:
            moneySum += dict[item]
        if moneySum > pay:
            print('支付金额不足，请重新支付。')
            return
        fee = float(pay - moneySum)
        for k in range(0, 7):
            b = fee / money[k]
            changes[money[k]] = int(b)
            fee = fee % money[k]
            k = k + 1
        print(changes)

if __name__ == '__main__':
    list_goods()                        #测试
    get_changes(['item01'],5)
    get_changes(['item01'],1)
    get_changes(['item01','item11','item13'],100)