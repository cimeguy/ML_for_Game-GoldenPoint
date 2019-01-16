#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目：获取当前天气情况

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et
import urllib.request
# http://www.webxml.com.cn/WebServices/WeatherWebService.asmx


def get_support_city(province):
    dic = bytes(urllib.parse.urlencode({'byProvinceName':province}), encoding='utf8')
    page = urllib.request.urlopen("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity", data = dic)
    lines = et.parse(page)
    root = lines.getroot()
    document = {}
    for child in root:
        for i in range(len(child.text)):
            if child.text[i] != ' ':
                pass
            else:
                document[child.text[:i]] = child.text[i+2:len(child.text)-1]
    return document


def get_weather(name):
    dic = bytes(urllib.parse.urlencode({'theCityName': name}), encoding='utf8')
    page = urllib.request.urlopen("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName", data=dic)
    lines = page.readlines()
    page.close()
    document = ""
    for line in lines:
        document = document + line.decode('utf-8')
    from xml.dom.minidom import parseString
    dom = parseString(document)
    strings = dom.getElementsByTagName("string")
    return strings[10].childNodes[0].data

print(get_support_city('陕西'))
if __name__ == "__main__":
    pass

 