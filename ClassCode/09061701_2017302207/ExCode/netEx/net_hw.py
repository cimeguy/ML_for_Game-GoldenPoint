#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目：获取当前天气情况
import re
import urllib.request
import urllib.parse

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# http://www.webxml.com.cn/WebServices/WeatherWebService.asmx


def get_support_city(province):
    province = urllib.parse.quote(province)
    data = "byProvinceName=" + province
    data = data.encode()
    url_ = "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity"
    r = urllib.request.urlopen(url_, data)
    tree = et.parse(r)
    root = tree.getroot()
    dict_city = {}
    for child in root:
        child = child.text
        for num in range(len(child)):
            if child[num] == '(':
                key = child[:num - 1]
                value = child[num + 1:num + 6]
                dict_city[key] = value
    return dict_city


def get_weather(name):
    url_ = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName'
    name = urllib.parse.quote(name)
    data = "theCityName=" + name
    data = data.encode()
    r = urllib.request.urlopen(url_, data)
    tree = et.parse(r)
    root = tree.getroot()
    str_city = ''
    for child in root:
        if re.search('%', child.text):
            return child.text

if __name__ == "__main__":
    pass

 