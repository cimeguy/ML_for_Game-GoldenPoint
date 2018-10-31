#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：词频统计
def word_freq(path):
    txt = open(path,'r').read().lower()     
    for ch in '!`~@#$%^&*()_-+=[]{}/?,.:\"<\/>':       
        txt = txt.replace(ch,' ')
    words = txt.split()
    object_list = []
    freq = {}
    high_freq=open('sight word.txt','r').read().lower().split()
    for h_word in words:
        #将不属于sight word的单词存储在列表中
        if h_word not in high_freq:
            object_list.append(h_word)
    for word in object_list:
        #创建字典的键，其值+1以统计词频
        freq[word]=freq.get(word,0)+1    
    items=list(freq.items())
    items.sort(key=lambda x:x[1],reverse=True)  #词频从大到小排序
    items=items[:10:]
    return items
	
if __name__ == '__main__':
    li = word_freq('../HowToBecomeAHacker.txt')       #测试
    print(li)

