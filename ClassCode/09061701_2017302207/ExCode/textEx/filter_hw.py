# -*- coding: UTF-8 -*-

import os
import string
import re

def filter_c_file(dir_path):
    _file_list = []
    # 得到该文件夹下的所有C文件
    fp = os.listdir(dir_path)
    for item in fp:
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):  # 只针对文件继续操作
            ext = os.path.splitext(item)[1]
            if ext in [".cpp", ".c"]:
                _file_list.append(item)
    # _file_list = ['filter0.cpp', 'filter1.cpp', 'filter2.cpp', 'filter3.cpp']
    for num in range(len(_file_list)):
        _file_list[num] = dir_path + '/' + _file_list[num]
    # 逐项处理
    for num in range(len(_file_list)):
        data_list = []
        fin = open(_file_list[num], 'r', encoding='gb18030', errors='ignore')
        # 读取每一行到列表data_list
        while True:
            line = fin.readline()
            if not line:
                break
            data_list.append(line)
        fin.close()
        # 检验data_list中的每一行

        for numofdata in range(len(data_list)):
            org_line = data_list[numofdata]
            if '*/' in org_line:

                if '/*' in org_line:
                    list_org_line = list(org_line)
                    for i in range(len(list_org_line)):
                        if list_org_line[i] == '/' and list_org_line[i + 1] == '*':
                            org_line = org_line[0:i]

                    data_list[numofdata] = org_line

                    break
                else:
                    data_list[numofdata] = ''
                    for numofdata1 in range(numofdata, 0, -1):

                        star_line = data_list[numofdata1]
                        if '/*' in star_line:

                            list_star_line = list(star_line)
                            for j in range(len(list_star_line)):
                                if list_star_line[j] == '/' and list_star_line[j + 1] == '*':
                                    star_line = star_line[:j]

                            data_list[numofdata1] = star_line

                            for numofdata2 in range(numofdata1 + 1, numofdata):
                                data_list[numofdata2] = ''
                            break
        data = ''

        for numlist in range(len(data_list)):
            line = data_list[numlist]
            if re.match('#include', line):
                line = ''
            if re.match('/', line):
                line = ''
            flag = flag1 = flag2 = True
            deadline = len(line)
            for number1 in range(len(line)):
                if line[number1] == '/':
                    deadline = number1
                    flag1 = flag2 = False
                    for number2 in range(number1):
                        if line[number2] == '\'' or line[number2] == '\"':
                            flag1 = True
                            break
                    for number3 in range(number1 + 1, len(line)):
                        if line[number3] == '\'' or line[number3] == '\"':
                            flag2 = True
                            break

                if flag1 and flag2:
                    flag = True
                else:
                    flag = False
                    break

            if not flag:
                line = line[:deadline]

            data += line

        for i in data:
            if i in string.whitespace:
                data = data.replace(i, ' ')
        data_list = data.split(' ')
        s = ''.join(data_list)
        file_name = _file_list[num][:-4]

        fout = open(file_name + '.txt', 'w')
        fout.write(s)
        fout.close()

    return None
if __name__ == '__main__':
    pass
