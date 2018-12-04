#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目11：实现数据库的操作
import sqlite3
import os

db_path = ""  # 全局变量，用于记录创建的数据库所在路径

def create_db(path):
    if os.path.exists(path):
        os.remove(path)
    connect = sqlite3.connect(path)
    c = connect.cursor()
    c1 = """
            CREATE TABLE Position(
                POSITIONID CHAR UNIQUE PRIMARY KEY,
                SALARY INT
            );
        """
    c2 = """
            CREATE TABLE Person(
                NAME CHAR(32),
                GENDER CHAR(2),
                BIRTH DATE,
                ID CHAR(18) UNIQUE PRIMARY KEY,
                POSITIONID CHAR,
                FOREIGN KEY (POSITIONID) REFERENCES Position(POSITIONID)
            );
        """
    flag = 0
    try:
        c.execute(c1)
        c.execute(c2)
        c.execute("INSERT INTO Position (POSITIONID,SALARY) VALUES ('A', 10000 );")
        c.execute("INSERT INTO Position (POSITIONID,SALARY) VALUES ('B', 6000 );")
        c.execute("INSERT INTO Position (POSITIONID,SALARY) VALUES ('C', 3000 );")
        c.execute("INSERT INTO Position (POSITIONID,SALARY) VALUES ('D', 1000 );")
        connect.commit()

    except sqlite3.Error as e:
        print('error!', e.args[0])
        flag = -1

    if flag == 0:
        global db_path
        db_path = path

    c.close()
    connect.close()

    return flag


def new_employee(person,level):
    if len(person) != 4:
        return -1

    global db_path
    connect = sqlite3.connect(db_path)
    c = connect.cursor()
    flag = 0
    try:
        c.execute("INSERT INTO Person VALUES (?,?,?,?,?);", person+tuple(level))
        connect.commit()
    except sqlite3.Error as e:
        print('error!', e.args[0])
        flag = -1

    c.close()
    connect.close()

    return flag


def delete_employee(person):
    global db_path;
    connect = sqlite3.connect(db_path)
    c = connect.cursor()
    flag = 0
    try:
        c.execute("DELETE FROM Person WHERE ID = ?", (person,))
        connect.commit()
    except sqlite3.Error as e:
        print('error!', e.args[0])
        flag = -1

    c.close()
    connect.close()

    return flag


def set_level_salary(level,salary):
    global db_path
    connect = sqlite3.connect(db_path)
    c = connect.cursor()
    flag = 0
    try:
        c.execute("UPDATE Position SET SALARY = ?  WHERE POSITIONID = ?", (salary,level))
        connect.commit()
    except sqlite3.Error as e:
        print('error!', e.args[0])
        flag = -1

    c.close()
    connect.close()

    return flag


def get_total_salary():
    global db_path
    connect = sqlite3.connect(db_path)
    c = connect.cursor()

    try:
        c1 = "SELECT COUNT(*) FROM Person WHERE POSITIONID = 'A';"
        c.execute(c1) 
        a = c.fetchall()[0][0]
        c1 = "SELECT COUNT(*) FROM Person WHERE POSITIONID = 'B';"
        c.execute(c1) 
        b = c.fetchall()[0][0]
        c1 = "SELECT COUNT(*) FROM Person WHERE POSITIONID = 'C';"
        c.execute(c1) 
        cc = c.fetchall()[0][0]
        c1 = "SELECT COUNT(*) FROM Person WHERE POSITIONID = 'D';"
        c.execute(c1) 
        d = c.fetchall()[0][0]
        
        total = 0
        c1 = "SELECT SALARY FROM Position WHERE POSITIONID = 'A';"
        c.execute(c1)
        total = total + c.fetchone()[0] * a

        c1 = "SELECT SALARY FROM Position WHERE POSITIONID = 'B';"
        c.execute(c1)
        total = total + c.fetchone()[0] * b

        c1 = "SELECT SALARY FROM Position WHERE POSITIONID = 'C';"
        c.execute(c1)
        total = total + c.fetchone()[0] * cc

        c1 = "SELECT SALARY FROM Position WHERE POSITIONID = 'D';"
        c.execute(c1)
        total = total + c.fetchone()[0] * d

        connect.commit()
    
    except sqlite3.Error as e:
        print('error!', e.args[0])
        total = -1

    c.close()
    connect.close()

    return total


if __name__ == "__main__":
    create_db('./test.db')
    new_employee(("tom","m","2018-09-01","123456789"),"A")
    new_employee(("too","f","2017-09-01","123456788"),"B")
    print(get_total_salary())
    delete_employee("123456788")
    print(get_total_salary())
    set_level_salary("A",2)
    print(get_total_salary())
