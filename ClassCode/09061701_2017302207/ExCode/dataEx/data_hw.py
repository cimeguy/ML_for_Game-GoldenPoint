#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十：二进制数据报文构建与解析
def pack_message(data_dict):
    data_list = list(data_dict.values())
    message = ''
    message = bytes([data_list[0], data_list[1]]) + data_list[2].encode('utf-8') + struct.pack('>L', data_list[3]) + \
              struct.pack('>L', data_list[4]) + bytes([data_list[5]])
    return message


def unpack_message(message):
    data_dict = {}
    data_dict['type'] = ord(message[:1])
    data_dict['csum'] = ord(message[1:2])
    data_dict['id'] = message[2:18].decode('utf-8')
    data_dict['dis1'] = struct.unpack('>L', message[18:22])[0]
    data_dict['dis2'] = struct.unpack('>L', message[22:26])[0]
    data_dict['count'] = ord(message[26:27])
    return data_dict


if __name__ == "__main__":
    pass