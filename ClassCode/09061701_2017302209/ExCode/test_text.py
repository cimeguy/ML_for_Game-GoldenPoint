#!/usr/bin/python
# -*- coding: UTF-8 -*-
from textEx.text_hw import *


# 题目：词频统计
def test_word():
    li = word_freq('testData/text0.txt')
    print(li)
    li = word_freq('testData/text1.txt')
    print(li)
    li = word_freq('testData/text2.txt')
    print(li)
    li = word_freq('testData/text3.txt')
    print(li)
    li = word_freq('testData/sight word.txt')
    print(li)
	

# 题目：morse code
def test_morse():
    s = morse_code("i am morse 258")
    # 正确输出：
    # . .       . -   - -       - -   - - -   . - .   . . .   .       . . - - -   . . . . .   - - - . .
    print(s)

if __name__ == '__main__':
    # test_morse()
    test_word()
