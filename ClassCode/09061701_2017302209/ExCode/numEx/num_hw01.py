#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os,sys

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

def d2b(decimal_int):
    mid = []
    while True:
        if decimal_int == 0: break
        decimal_int, rem = divmod(decimal_int, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])

def b2d(binary_string):
    return str(int(binary_string, 2))
	
	
def fibonacci_recursion(number):
   return -1
   
   
def fibonacci_loop(number):
    return -1
	
if __name__ == '__main__':
    print(fibonacci_recursion(10))
    print(fibonacci_loop(10))
