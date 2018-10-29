#!/usr/bin/python
# -*- coding: UTF-8 -*-


def word_freq(path):
    txt = open(path,'r').read()
    txt = txt.lower()      #大写字母变小写
    for ch in '!`~@#$%^&*()_-+=[]{}/?,.<\/>':        #用空格代替符号
        txt = txt.replace(ch,' ')
    words = txt.split()
    freq={}
    for word in words:
        freq[word]=freq.get(word,0)+1    #创建字典的键，其值+1以统计词频
    items=list(freq.items())
    items.sort(key=lambda x:x[1],reverse=True)  #词频从大到小排序
    items=items[:10:]
    print(items)
	
if __name__ == '__main__':
    word_freq('../HowToBecomeAHacker.txt')       #测试


