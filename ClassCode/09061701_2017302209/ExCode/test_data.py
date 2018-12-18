#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from dataEx.xml_hw import *
from dataEx.db_hw import *
from dataEx.data_hw import *

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


# 单元测试
class TestXmlFunc(unittest.TestCase):
    # 题目：XML文件的生成和解析
    def test_Xml1(self):
        path = "./created.xml"
        if os.path.exists(path):
            os.remove(path)

        create_xml(path)
        self.assertTrue(os.path.exists(path))

        d = parse_xml(path)
        self.assertDictEqual(d,{'tilemap service': 'http://tms.osgeo.org/1.0.0 ', 'title': 'default', 'tileset count': 6, 'tileset max': 5})

        # 修改XML文件
        tree = et.parse(path)  # 解析xml文件，返回ElementTree对象
        root = tree.getroot()  # 获取根节点
        item = root.find("tilesets")
        et.SubElement(item, "tileset",{"href":"","order":"10","units-per-pixel":"10.588"})
        tree.write(path)

        d = parse_xml(path)
        self.assertDictEqual(d,{'tilemap service': 'http://tms.osgeo.org/1.0.0 ', 'title': 'default', 'tileset count': 7, 'tileset max': 10})


    # 题目：二进制数据报文构建与解析
    def test_data(self):
        data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
        data = pack_message(data_dict)
        self.assertEquals(data, b'2\x01abcdefghigklmnop\x00\x00\x01,\x00\x00\x00d\x14')

        new_dict = unpack_message(data)
        self.assertDictEqual(new_dict,data_dict)


    # 题目：实现数据库的操作
    def test_db(self):
        path = './test.db'
        if os.path.exists(path):
            os.remove(path)

        create_db(path)
        new_employee(("tom","m","2018-09-01","123456789"),"A")
        new_employee(("too","f","2017-09-01","123456788"),"B")

        self.assertEquals(get_total_salary(),16000)
        delete_employee("123456788")
        self.assertEquals(get_total_salary(),10000)

        set_level_salary("A",2)
        self.assertEquals(get_total_salary(),2)


if __name__ == '__main__':
    unittest.main()