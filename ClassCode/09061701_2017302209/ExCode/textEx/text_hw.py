#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目五：摩斯码生成器
codebook = {
    'A':"@#",
    'B':"#@@@",
    'C':"#@#@",
    'D':"#@@",
    'E':"@",
    'F':"@@#@",
    'G':"##@",
    'H':"@@@@",
    'I':"@@",
    'J':"@###",
    'K':"#@#",
    'L':"@#@@",
    'M':"##",
    'N':"#@",
    'O':"###",
    'P':"@##@",
    'Q':"##@#",
    'R':"@#@",
    'S':"@@@",
    'T':"#",
    'U':"@@#",
    'V':"@@@#",
    'W':"@##",
    'X':"#@@#",
    'Y':"#@##",
    'Z':"##@@",
    '1':"@####",
    '2':"@@###",
    '3':"@@@##",
    '4':"@@@@#",
    '5':"@@@@@",
    '6':"#@@@@",
    '7':"##@@@",
    '8':"###@@",
    '9':"####@",
    '0':"#####",
}

def morse_code(usr_str):
    morse = ""
    s = usr_str.upper()
    for c in s:
        if c == ' ':
            continue
        morse += codebook[c]+" "
    return morse
		

# 题目六：词频统计
from collections import Counter
def word_freq(path):
    txt = open(path,'r').read().lower()     
    for ch in '!`~@#$%^&*()_-+=[]{}/?,.:\"<\/>':       
        txt = txt.replace(ch,' ')
    words = txt.split()
    object_list = []

    high_freq=open('testData/sight word.txt','r').read().lower().split()
    for h_word in words:
        # 将不属于sight word的单词存储在列表中
        if h_word not in high_freq:
            object_list.append(h_word)
    '''
    # 字典写法
    freq = {}
    for word in object_list:
        # 创建字典的键，其值+1以统计词频
        freq[word]=freq.get(word,0)+1    
    items=list(freq.items())
    items.sort(key=lambda x:x[1],reverse=True)  #词频从大到小排序
    items=items[:10:]
    return items
    '''
    # Counter写法
    return Counter(object_list).most_common(10)
	
if __name__ == '__main__':
    li = word_freq('../HowToBecomeAHacker.txt')       #测试
    print(li)

