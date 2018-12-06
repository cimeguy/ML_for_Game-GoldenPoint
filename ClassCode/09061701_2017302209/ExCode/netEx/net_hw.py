#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：获取当前天气情况
import requests

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# http://www.webxml.com.cn/WebServices/WeatherWebService.asmx


def get_support_city(province):
    url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity'
    body = {"byProvinceName": province}
    response = requests.post(url, data = body)
    # print(response.text)

    city_dict = dict()
    if response.status_code == 200:
        root = et.fromstring(response.text)

        for city in root:
            l = city.text.split(" ")
            city_dict[l[0]] = l[1][1:-1]

    # print(city_dict)
    return city_dict


def get_weather(name):

    url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName'
    body = {"theCityName": name}
    response = requests.post(url, data = body)

    des = ""
    if response.status_code == 200:
        root = et.fromstring(response.text)
        for city in root:
            if city.text.find("今日天气实况") > -1:
                des = city.text

    return des

if __name__ == "__main__":
   # print(get_support_city(""))
   citys = get_support_city("陕西")
   name = "西安"
   if name in citys:
       print(get_weather(name))
       # get_weather(citys[name])

 