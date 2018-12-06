# -*- coding: UTF-8 -*-

import os


# 遍历dir_path，获取所有以[".cpp", ".c"]结尾的文件路径
def find_source_file(dir_path):
    _file_list = []
    fp = os.listdir(dir_path)  # 得到该文件夹下的所有文件
    for item in fp:
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path): # 只针对文件继续操作
            ext = os.path.splitext(item)[1]
            if ext in [".cpp", ".c"]:
                _file_list.append(item_path)

    return _file_list


# 删除每行中的回车换行，以及空格
def fiter_blankline_space(lines):
    l = []
    for line in lines:
        l.append("".join(line.split()))
    return l


# 删除空行
def filter_blank_line(lines):
    l = []
    for line in lines:
        if line != "\n":
            l.append(line)
    return l


# 删除每行中的空格
def filter_space_tab(lines):
    l = []
    for line in lines:
        s = line.replace(" ", "")
        s = s.replace("\t", "")
        l.append(s)
    return l


# 删除块注释
# 首先查找本行内的块注释符号“/*”，第一个块注释的前面只能有偶数个双引号，以避免起始块出现在字符串内部
# 认定为块注释开始，在本行内寻找匹配的块注释结束符号"*/"；如果没有读入新行，直到找到结束符号“*/”；
# 两者之间的文本被去除，结束符号如果存在后续文本，则重新查找块注释开始符号
def filter_block_comment(lines):
    l = []
    i = 0
    line_count = len(lines)
    find_start_block = True

    while i < line_count:
        line = lines[i]
        # 在一行中查找起始块注释
        if find_start_block:
            start = 0  # 设置查找起始位置
            while start <= len(line):
                ret = line.find("/*", start)
                if ret != -1:  # 找到一个块注释起始块
                    pq = line[:ret].count('"')
                    if pq % 2 == 0:  # 第一个块注释的前面只能有偶数个双引号，避免起始块出现在字符串内部
                        if has_line_comment(line[:ret]):
                            # 存在特殊情况： "// /*" 这种注释，应跳过，进入下一行重新查找块注释
                            find_start_block = True
                            l.append(line)
                            i += 1
                            break

                        ret1 = line.find("*/", ret+2)
                        if ret1 != -1:  # 找到对应的结束块，移除整个注释块，再重新查找起始块
                            line = line[:ret]+line[ret1+2:]
                            start = ret
                            find_start_block = True
                        else:  # 本行未找到对应的结束块，应该在下一行中查找结束块
                            line = line[:ret]
                            l.append(line)
                            find_start_block = False
                            i += 1
                            break
                    else:  # 找到的起始块不是合理的起始块，继续查找起始块
                        start = ret+2
                else:  # 本行未找到注释起始块，退出本循环体，进入下一行
                    find_start_block = True
                    i += 1
                    l.append(line)
                    break
        else:  # 查找结束块，如果是正常的块注释，只需查找第一个结束块即可
            ret = line.find("*/", 0)
            if ret != -1:  # 找到结束块，结束块之前的内容被移除，重新在本行查找起始块
                lines[i] = line[ret+2:]  # 将本行更新，前面匹配的块注释内容被删除，下一轮循环将重新在本行查找起始块
                find_start_block = True
            else:  # 未找到结束块，进入下一行继续查找，本行内容默认为块注释内部，被移除
                find_start_block = False
                i += 1

    return l


# 查找本行内是否存在行注释
def has_line_comment(line):
    start = 0  # 设置查找起始位置
    while start <= len(line):
        ret = line.find("//", start)
        if ret != -1:  # 找到一个行注释标识
            pq = line[:ret].count('"')
            if pq % 2 == 0:  # 行注释的前面只能有偶数个双引号，避免起始块出现在字符串内部
                 return True
            else:  # 找到的不是合理的行注释，继续查找起始块
                 start = ret+2
        else:  # 未能找到一个行注释标识
            break

    return False


# 查找本行内的行注释符号“//”，行注释的前面只能有偶数个双引号，避免起始块出现在字符串内部
# 删除//及后续内容
# 需注意行注释符号可能出现在块注释中，所以这里先过滤了块注释
def filter_line_comment(lines):
    l = []
    for line in lines:
        start = 0  # 设置查找起始位置
        while start <= len(line):
            ret = line.find("//", start)
            if ret != -1:  # 找到一个行注释标识
                pq = line[:ret].count('"')
                if pq % 2 == 0:  # 行注释的前面只能有偶数个双引号，避免起始块出现在字符串内部
                    # if ret == 0 or line[ret - 1] in [")", "}", "{", ";"]:
                    line = line[:ret]  # 合理的行注释符号，取非注释部分
                    l.append(line)
                    break  # 行注释后面的字符全部去掉后，直接进入下一行
                else:  # 找到的不是合理的行注释，继续查找起始块
                    start = ret+2
            else:  # 未能找到一个行注释标识
                l.append(line)
                break

    return l


# 每行中只允许一行#include语句
def filter_include(lines):
    l = []
    for line in lines:
        ret = line.find("#include", 0)
        if ret != 0:  # 不是以#include开头，不是include语句
            l.append(line)
    return l


def filter_return(lines):
    l = []
    for line in lines:
        l.append(line.rstrip("\n"))
    return l


# 返回的是字符串
def filter_one_file(file_path):

    pattern = "111111"

    with open(file_path,encoding='gb18030',errors="ignore") as f:
        _code_lines = f.readlines()

        if pattern[0] == "1":  # 首先删除每行中的空格
            _code_lines = filter_space_tab(_code_lines)
        if pattern[1] == "1":  # 再删除块注释
            _code_lines = filter_block_comment(_code_lines)
        if pattern[2] == "1":  # 再删除行注释
            _code_lines = filter_line_comment(_code_lines)
        if pattern[3] == "1":  # 再删除include
            _code_lines = filter_include(_code_lines)
        if pattern[4] == "1":  # 再删除空行
            _code_lines = filter_blank_line(_code_lines)
        if pattern[5] == "1":  # 删除回车换行
            _code_lines = filter_return(_code_lines)

    return "".join(_code_lines)


def filter_c_file(dir_path):
    # 查找需要处理的源文件
    source_files = find_source_file(dir_path)

    # 针对每个文件进行过滤
    for item in source_files:
        base_name = os.path.basename(item)
        file_name = os.path.splitext(base_name)[0]
        new_file_name = os.path.join(dir_path, file_name+".txt")

        lines = filter_one_file(item)

        with open(new_file_name, "w+", encoding='gb18030',errors="ignore") as nf:
            nf.writelines(lines)

if __name__ == '__main__':
    dir_path = "./../testData"
    filter_c_file(dir_path)
