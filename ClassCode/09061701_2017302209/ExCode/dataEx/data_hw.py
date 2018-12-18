#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十：二进制数据报文构建与解析
def pack_message(data_dict):
    a = data_dict['type']
    b = data_dict['csum']
    c = data_dict['id']
    d = data_dict['dis1']
    e = data_dict['dis2']
    f = data_dict['count']
    pack_data = struct.pack('>BB16sllB', a, b, c.encode('utf-8'), d, e, f)  # pack要求字符串为byte类型，所以才哟功能encode
    return pack_data


def unpack_message(message):
    unpack_data = struct.unpack('>BB16sllB', message)
    new_dict = dict()
    new_dict['type'] = unpack_data[0]
    new_dict['csum'] = unpack_data[1]
    new_dict['id'] = unpack_data[2].decode('utf-8')
    new_dict['dis1'] = unpack_data[3]
    new_dict['dis2'] = unpack_data[4]
    new_dict['count'] = unpack_data[5]

    return new_dict


def test_data():
    data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
    data = pack_message(data_dict)
    print(len(data))
    print(data)
    new_dict = unpack_message(data)
    print(new_dict)


if __name__ == "__main__":
    test_data()