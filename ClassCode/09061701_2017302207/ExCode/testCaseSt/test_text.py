#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from textEx.text_hw import *
from textEx.filter_hw import *


# 单元测试
class TestTextFunc(unittest.TestCase):

    # 题目：词频统计
    def test_word(self):

        li = word_freq( './testData/text0.txt')
        self.assertListEqual(li,[('b', 16), ('shorts', 4), ('ok', 4), ('dollars', 4), ('welcome', 2), ('twenty', 2), ('thanks', 2), ('purple', 2), ('nice', 2), ('need', 2)])
        li = word_freq( './testData/sight word.txt')
        self.assertListEqual(li,[])

    def test_word_1(self):
        li = word_freq('./testData/text0.txt')
        self.assertListEqual(li, [('b', 16), ('shorts', 4), ('ok', 4), ('dollars', 4), ('welcome', 2), ('twenty', 2),
                                  ('thanks', 2), ('purple', 2), ('nice', 2), ('need', 2)])

    def test_word_2(self):
        li = word_freq('./testData/text1.txt')
        self.assertListEqual(li, [('tara', 11), ('arabic', 6), ('women', 5), ('esl', 5), ('each', 5), ('students', 4),
                                  ('rose', 4), ('other', 4), ('iraq', 4), ('day', 4)])

    def test_word_3(self):
        li = word_freq('./testData/text2.txt')
        self.assertListEqual(li,
                             [('hacker', 78), ('hackers', 61), ('learn', 37), ('—', 33), ('source', 30), ('other', 28),
                              ('software', 26), ('linux', 26), ('most', 25), ('culture', 25)])

    def test_word_4(self):
        li = word_freq('./testData/text3.txt')
        self.assertListEqual(li, [('1000', 5), ('place', 4), ('house', 4), ('back', 4), ('visit', 3), ('himself', 3),
                                  ('happy', 3), ('great', 3), ('dogs', 3), ('wagging', 2)])

    def test_word_5(self):
        li = word_freq('./testData/sight word.txt')
        self.assertListEqual(li, [])
    # 题目：morse code
    def test_morse(self):
        s = morse_code("i am morse 258")
        self.assertEqual(s,". .       . -   - -       - -   - - -   . - .   . . .   .       . . - - -   . . . . .   - - - . .")


    def test_filter(self):
        dir_path = "./testData"
        _file_list = []
        # 得到该文件夹下的所有C文件
        fp = os.listdir(dir_path)
        for item in fp:
            item_path = os.path.join(dir_path, item)
            if os.path.isfile(item_path): # 只针对文件继续操作
                ext = os.path.splitext(item)[1]
                if ext in [".cpp", ".c"]:
                    _file_list.append(item)
        # 删除C文件对应存在的txt文件
        for item in _file_list:
            item_path = os.path.join(dir_path, item.split(".")[0] + ".txt")
            if os.path.exists(item_path):
                os.remove(item_path)
        filter_c_file(dir_path)
        # 查看txt文件的存在性
        for item in _file_list:
            item_path = os.path.join(dir_path, item.split(".")[0] + ".txt")
            self.assertTrue(os.path.exists(item_path))
        # 比对文件
        for item in _file_list:
            txt_path = os.path.join(dir_path, item.split(".")[0] + ".txt")
            txtv_path = os.path.join(dir_path, item.split(".")[0] + "_v.txt")

            with open(txt_path, "r", encoding='gb18030',errors="ignore") as nf:
                lines = nf.readlines()
            with open(txtv_path, "r", encoding='gb18030',errors="ignore") as nf:
                vlines = nf.readlines()

            self.assertListEqual(lines,vlines)


if __name__ == '__main__':
    unittest.main()