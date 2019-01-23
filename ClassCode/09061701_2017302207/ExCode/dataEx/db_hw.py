#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目11：实现数据库的操作
import sqlite3
import os

db_path = ""  # 全局变量，用于记录创建的数据库所在路径

def create_db(path):
    global db_path
    db_path = path
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    curs = conn.cursor()
    try:
        curs.execute('''CREATE TABLE Person
                    (NAME VARCHAR (32),
                    GENDER VARCHAR (2),
                    BIRTH MESSAGE_TEXT ,
                    ID VARCHAR (18) PRIMARY KEY,
                    POSITIONID VARCHAR,
                     foreign key (POSITIONID) references Position)''')
        curs.execute('''CREATE TABLE Position
                        (POSITIONID VARCHAR PRIMARY KEY CHECK (POSITIONID in ('A', 'B', 'C', 'D')),
                        SALARY INT )''')
        set_level_salary('A', 10000)
        set_level_salary('B', 6000)
        set_level_salary('C', 3000)
        set_level_salary('D', 1000)
        conn.commit()
        conn.close()
        return 0
    except:
        return -1


def new_employee(person,level):
    conn_insert = sqlite3.connect(db_path)
    curs_insert = conn_insert.cursor()
    values_tupe = person + tuple(level)
    try:
        ins = 'INSERT INTO Person (NAME,GENDER,BIRTH,ID,POSITIONID) VALUES (?, ?, ?,?,? )'
        curs_insert.execute(ins, values_tupe)
        conn_insert.commit()
        conn_insert.close()
        return 0
    except:
        conn_insert.commit()
        conn_insert.close()
        return -1


def delete_employee(person):
    conn_delete = sqlite3.connect(db_path)
    curs_delete = conn_delete.cursor()
    try:
        str_delete = "delete from Person WHERE ID ==? "
        curs_delete.execute(str_delete, (person,))

        conn_delete.commit()
        conn_delete.close()
    except:
        conn_delete.close()
        return -1


def set_level_salary(level,salary):
    set_tuple1 =  salary,level
    set_tuple =  level,salary

    conn = sqlite3.connect(db_path)
    curs = conn.cursor()

    check = '''SELECT * FROM POSITION '''
    results =  curs.execute(check)
    res = results.fetchall()

    for r in res:
        if r[0] ==level:

            ins2 = 'DELETE FROM Position WHERE POSITIONID = ?'
            curs.execute(ins2,(level,))
            conn.commit()

    try:
        # ins = 'UPDATE Position SET SALARY = ? WHERE POSITIONID =?'
        ins = 'INSERT INTO Position(POSITIONID,SALARY) VALUES(?,?)'
        curs.execute(ins, set_tuple)
        conn.commit()
        conn.close()
        return 0
    except:
        return -1


def get_total_salary():
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    curs.execute("select POSITIONID from Person")
    res = curs.fetchall()
    try:
        sum = []
        for num in range(len(res)):
            key = res[num]

            conn1 = sqlite3.connect(db_path)
            curs1 = conn1.cursor()
            curs1.execute("select SALARY from Position WHERE POSITIONID ==?", key)
            res1 = curs1.fetchone()
            sum.append(res1[0])
        sumsalary = 0
        conn.close()
        for number in sum:
            sumsalary += number
        return sumsalary
    except:
        conn.close()
        return -1


if __name__ == "__main__":
    path = './test.db'
    if os.path.exists(path):
        os.remove(path)

    create_db(path)

    print(new_employee(("tom", "m", "2018-09-01", "123456789"), "A"))
    new_employee(("too", "f", "2017-09-01", "123456788"), "B")

    print(get_total_salary())
    delete_employee("123456788")
    set_level_salary("A", 2)
    print(get_total_salary())