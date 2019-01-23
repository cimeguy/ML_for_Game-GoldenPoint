#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
# 题目五：摩斯码生成器
def morse_code(usr_str):
    usr_str = usr_str.upper()
    usr_strsplit = usr_str.split(' ')
    morse_dict = {
        'A': '. -', 'B': '- . . .', 'C': '- . - .', 'D': '- . .', 'E': '.', 'F': '. . - .', 'G': '- - .',
        'H': '. . . .', 'I': '. .', 'J': '. - - -', 'K': '- . -', 'L': '. - . .', 'M': '- -', 'N': '- .',
        'O': '- - -', 'P': '. - - .', 'Q': '- - . -', 'R': '. - .', 'S': '. . .', 'T': '-',
        'U': '. . -', 'V': '. . . -', 'W': '. - -', 'X': '- . . -', 'Y': '- . - -', 'Z': '- - . .',
        '1': '. - - - -', '2': '. . - - -', '3': '. . . - -', '4': '. . . . -', '5': '. . . . .',
        '6': '- . . . .', '7': '- - . . .', '8': '- - - . .', '9': '- - - - .', '0': '- - - - -'
    }
    morse_str = ''
    for str in usr_strsplit:
        for c in str:
            morse_str += (morse_dict.get(c) + '   ')
        morse_str += ' ' * 4
    morse_str = morse_str[:len(morse_str) - 7]
    return morse_str
		

# 题目六：词频统计
def word_freq(path):
    dict_ = {}
    data = ''
    fin = open(path, 'rt')
    while True:
        line = fin.readline()
        if not line:
            break
        data += line
    fin.close()
    for i in data:
        if i in string.whitespace:
            data = data.replace(i, ' ')

    data = data.replace(',', ' ')
    data = data.replace('.', ' ')
    data = data.replace(':', ' ')
    data = data.replace('\n', ' ')
    data = data.replace('"', ' ')
    data = data.replace('?', ' ')
    data = data.replace('-', ' ')
    data = data.replace('!', ' ')
    data = data.replace('(', ' ')
    data = data.replace(')', ' ')
    data = data.replace('/', ' ')

    data = data.lower()
    line_list = data.split(' ')
    print(line_list)
    finsight = open('../testCaseSt/testData/sight word.txt', 'rt')
    sights = finsight.read()
    finsight.close()
    sights = sights.lower()
    sights_list = sights.split(' ')

    for num in range(len(line_list)):
        dict_[line_list[num]] = line_list.count(line_list[num])
    for num2 in range(len(sights_list)):
        if sights_list[num2] in line_list and not sights_list[num2] == '':
            del dict_[sights_list[num2]]
    del dict_['']

    sort_dict_list = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    s = dict(sort_dict_list)
    list_values = list(s.values())
    new_dict = {}
    for value_s in list_values:
        keylist = []
        for key in s:
            if s[key] == value_s:
                keylist += [key]
        keylist = sorted(keylist, reverse=True)
        for num3 in range(len(keylist)):
            new_dict[keylist[num3]] = value_s
    list_new = list(new_dict.items())
    return list_new[:10]


if __name__ == '__main__':
    li = word_freq('../testCaseSt/testData/text2.txt')
    print(li)

# [('hacker', 78), ('hackers', 61), ('learn', 37), ('—', 33), ('source', 30), ('other', 28),
# ('software', 26), ('linux', 26), ('most', 25), ('culture', 25)])