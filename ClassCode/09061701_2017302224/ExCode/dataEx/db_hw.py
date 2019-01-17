#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目11：实现数据库的操作
import sqlite3
import os

import sqlite3
db_path = ""  # 全局变量，用于记录创建的数据库所在路径


def create_db(path):
    try:
        if os.path.exists(path):
            os.remove(path)
        db = sqlite3.connect(path)
        db.execute("CREATE TABLE Person(姓名NAME text,性别GENDER text,生日BIRTH text,身份证号ID text primary key,岗位POSITIONID text)")
        db.execute("CREATE TABLE Position(岗位名称POSITIONID text primary key,薪水SALARY int)")
        db.commit()
        db.close()
        return 0
    except:
        return -1


def new_employee(person,level):
    try:
        Person = [(person[0], person[1], person[2], person[3], level)]
        db = sqlite3.connect(db_path)
        salary = {'A': 10000, 'B': 6000, 'C': 3000, 'D': 1000}
        c = db.cursor()
        c.executemany('INSERT INTO Person VALUES (?, ?, ?, ?, ?)', Person)
        db.commit()
        set_level_salary(level, salary[level])
        db.close()
        return 0
    except:
        return -1


def delete_employee(person):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        salary = {'A': 10000, 'B': 6000, 'C': 3000, 'D': 1000}
        c.execute('SELECT 岗位POSITIONID FROM Person WHERE 身份证号ID=%s'%person)
        b = c.fetchall()
        c.execute('DELETE FROM Position WHERE 薪水SALARY=%s'%salary[b[0][0]])
        c.execute('DELETE FROM Person WHERE 身份证号ID=%s'%person)
        db.commit()
        db.close()
        return 0
    except:
        return -1


def set_level_salary(level,salary):
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        Position1 = [(level, salary)]
        c.executemany('INSERT INTO Position VALUES (?, ?)', Position1)
        db.commit()
        return 0
    except:
        return -1


def get_total_salary():
    try:
        db = sqlite3.connect(db_path)
        c = db.cursor()
        c.execute("SELECT * FROM Position ORDER BY 薪水SALARY")
        b = c.fetchall()
        a = 0
        for i in range(len(b)):
            a += b[i][1]
        db.commit()
        db.close()
        return a
    except:
        return -1


if __name__ == "__main__":
    pass
