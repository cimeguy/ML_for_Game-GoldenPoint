#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dataEx.xml_hw import *
from dataEx.db_hw import *


def test_xml():
    create_xml("created.xml")
    parse_xml("created.xml")
	
	
def test_data():
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
    test_data()
