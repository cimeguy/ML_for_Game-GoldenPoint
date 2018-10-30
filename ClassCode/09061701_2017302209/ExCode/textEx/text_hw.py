#!/usr/bin/python
# -*- coding: UTF-8 -*-


def word_freq(path):
    txt = open(path,'r').read()
    txt = txt.lower()      #大写字母变小写
    for ch in '!`~@#$%^&*()_-+=[]{}/?,.:\"<\/>':        #用空格代替符号
        txt = txt.replace(ch,' ')
    words = txt.split()
    i=0
    high_freq=open('sight word.txt','r').read()
    while i<len(words):
    #删除高频词
        if words[i] in high_freq.split():
            words.remove(words[i])
            i=0
            continue
        else:
            i=i+1
    freq={}
    for word in words:
        freq[word]=freq.get(word,0)+1    #创建字典的键，其值+1以统计词频
    items=list(freq.items())
    items.sort(key=lambda x:x[1],reverse=True)  #词频从大到小排序
    items=items[:10:]
    print(items)
	
if __name__ == '__main__':
    word_freq('../HowToBecomeAHacker.txt')       #测试


