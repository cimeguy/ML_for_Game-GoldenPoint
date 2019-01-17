#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十：二进制数据报文构建与解析
def pack_message(data_dict):
    dic = bytes()
    for item in data_dict.items():
        if 50 == item[1]:
            dic += struct.pack('b', item[1])
        elif 1 == item[1]:
            dic += struct.pack('b', item[1])
        elif 'str' in str(type(item[1])):
            dic += bytes(str(item[1]),encoding="utf8")
        elif 300 == item[1]:
            dic += struct.pack('>I', item[1])
        elif 100 == item[1]:
            dic += struct.pack('>I', item[1])
        elif 20 == item[1]:
            dic += struct.pack('b', item[1])
    return dic


def unpack_message(message):
    i = 0
    dic = {}
    dic1 = struct.unpack('bb', message[i:i+2])
    dic['type'] = dic1[0]
    dic['csum'] = dic1[1]
    i += 2
    dic2 = message[i:i+16].decode()
    dic['id'] = dic2
    i += 16
    dic3 = struct.unpack('>II',message[i:i+8])
    dic['dis1'] = dic3[0]
    dic['dis2'] = dic3[1]
    i += 8
    dic4 = struct.unpack('b',message[i:])
    dic['count'] = dic4[0]
    return dic


if __name__ == "__main__":
    pass
