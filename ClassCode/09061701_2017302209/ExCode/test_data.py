#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from dataEx.xml_hw import *
from dataEx.db_hw import *
from dataEx.data_hw import *


def test_xml():
    path = "created.xml"
    if os.path.exists(path):
        os.remove(path)

    create_xml("created.xml")
    print(parse_xml("created.xml"))


def test_data():
    data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
    data = pack_message(data_dict)
    print(len(data))
    print(data)
    new_dict = unpack_message(data)
    print(new_dict)

	
def test_db():
    ret = create_db('./test.db')
    print(ret)
    ret = new_employee(("tom","m","2018-09-01","123456789"),"A")
    print(ret)
    ret = new_employee(("too","f","2017-09-01","123456788"),"B")
    print(ret)	
    print(get_total_salary())
    ret = delete_employee("123456788")
    print(ret)	
    print(get_total_salary())
    ret = set_level_salary("A",2)
    print(ret)
    print(get_total_salary())

if __name__ == '__main__':
    # test_db()
    test_xml()
    test_data()