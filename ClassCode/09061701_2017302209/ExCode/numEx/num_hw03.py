#!/usr/bin/python
# -*- coding: UTF-8 -*-


from math import radians, cos, sin, asin, sqrt
p1=();
p2=();
def sphere_distance(p1, p2):
#def sphere_distance(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    # 将十进制度数转化为弧度
    lon1=p1[0];
    lat1=p1[1];
    lon2=p2[0];
    lat2=p2[1];
    if lon1<0 or lon1 >90 or lon2<0 or lon2 >90 or lat1<0 or lat1>180 or lat1<0 or lat2>180:
        print('Parameter Error.')
    else:

        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # 地球平均半径，单位为公里
        return c * r

# (112.3, 25.3, 152.6, 23.4)
# 4072.805450203038


if __name__ == '__main__':
    dis = sphere_distance((12.3, 25.3), (52.6, 23.4))
    print(dis)

