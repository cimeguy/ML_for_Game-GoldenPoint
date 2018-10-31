#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：实现数据库的操作
import sqlite3
import os


def create_db(path):
    try:
        if(os.path.exists(path)):
            os.unlink(path)
        connect = sqlite3.connect(path)
        c = connect.cursor()
        c1 = '''
        CREATE TABLE Position(
        POSITIONID CHAR UNIQUE PRIMARY KEY,
        SALARY INT
        );
        '''
        c2 = '''
        CREATE TABLE Person(
        NAME CHAR(32),
        GENDER CHAR(2),
        BIRTH DATE,
        ID CHAR(18) UNIQUE PRIMARY KEY,
        POSITIONID CHAR,
        FOREIGN KEY (POSITIONID) REFERENCES Position(POSITIONID)
        );
        '''
        c.execute(c1)
        c.execute(c2)
        c.execute("INSERT INTO Position (POSITIONID,SALARY) \
        VALUES ('A', 10000 );")
        c.execute("INSERT INTO Position (POSITIONID,SALARY) \
        VALUES ('B', 6000 );")
        c.execute("INSERT INTO Position (POSITIONID,SALARY) \
        VALUES ('C', 3000 );")
        c.execute("INSERT INTO Position (POSITIONID,SALARY) \
        VALUES ('D', 1000 );")
        connect.commit()

    except:
        return "error"
    else:
        return "ok"

def new_employee(person,level):
    try:
        connect = sqlite3.connect("./test.db")
        c = connect.cursor()
        c1 = "INSERT INTO Person (NAME,GENDER,BIRTH,ID,POSITIONID) \
        VALUES ('"+person[0]+"', '"+person[1]+"', '"+person[2]+"', '"+person[3]+"', '"+level+"');"
        c.execute(c1)
        connect.commit()
    except Exception as e:
        return str(e)
    else:
        return "ok"

def delete_employee(person):
    try:
        connect = sqlite3.connect("./test.db")
        c = connect.cursor()
        c1 = "DELETE FROM Person WHERE ID = "+person+";"
        c.execute(c1)
        connect.commit()
    except Exception as e:
        return str(e)
    else:
        return "ok"

def set_level_salary(level,salary):
    try:
        connect = sqlite3.connect("./test.db")
        c = connect.cursor()
        c1 = "UPDATE Position SET SALARY = "+str(salary)+" WHERE POSITIONID = '"+level+"';"
        c.execute(c1)
        connect.commit()
    except:
        return "error"
    else:
        return "ok"

def get_total_salary():
    try:
        connect = sqlite3.connect("./test.db")
        c = connect.cursor()

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
    
    except:
        return -1
    else:
        return total

def main():
    create_db('./test.db')
    new_employee(("tom","m","2018-09-01","123456789"),"A")
    new_employee(("too","f","2017-09-01","123456788"),"B")
    print(get_total_salary())
    delete_employee("123456788")
    print(get_total_salary())
    set_level_salary("A",2)
    print(get_total_salary())

if __name__ == "__main__":
    main()
