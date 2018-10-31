#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：获取当前天气情况
import requests


def get_weather(cityname):
    try:
        r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + cityname)
        data = r.json()['data']['forecast'][0]
    except:
        return {}
    else:
        return data

def main():
    res = get_weather('北京')
    print(res)

if __name__ == "__main__":
    main()
 