#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 题目五：摩斯码生成器
def morse_code(usr_str):
    stri = ''
    usr_str = usr_str.lower()
    morse = {'a':'. -','b':'- . .','c':'- . - .','d':'- . .','e':'.',
             'f':'. . - .','g':'- - .','h':'. . . .','i':'. .','j':'. - - -',
             'k':'- . -','l':'. - . .','m':'- -','n':'- .','o':'- - -',
             'p':'. - - .','q':'- - . -','r':'. - .','s':'. . .','t':'.','u':'. . -',
             'v':'. . . -','w':'. - -','x':'- . . -','y':'- . - -','z':'- - . .',
             '1':'. - - - -','2':'. . - - -','3':'. . . - -','4':'. . . . -',
             '5':'. . . . .','6':'- . . . .','7':'- - . . .','8':'- - - . .',
             '9':'- - - - .','0':'- - - - -',' ':' '}
    for i in range(0, len(usr_str)):
        a = usr_str[i]
        if usr_str[i] != ' ':
            stri += morse[a] + '   '
        else:
            stri += morse[a] + '   '
    stri = stri.rstrip('   ')
    return stri


# 题目六：词频统计
def word_freq(path):
    import collections
    text = open(path).read()
    li = str(text)
    fil = {'a': 1, 'and': 1, 'away': 1, 'big': 1, 'blue': 1, 'can': 1, 'come': 1, 'down': 1, 'find': 1,
           'for': 1, 'funny': 1, 'go': 1, 'help': 1, 'here': 1, 'i': 1, 'in': 1, 'is': 1, 'it': 1, 'jump': 1,
           'little': 1, 'look': 1, 'make': 1, 'me': 1, 'my': 1, 'not': 1, 'one': 1, 'play': 1, 'red': 1,
           'run': 1, 'said': 1, 'see': 1, 'the': 1, 'three': 1, 'to': 1, 'two': 1, 'up': 1, 'we': 1, 'where': 1,
           'yellow': 1, 'you': 1, 'all': 1, 'am': 1, 'are': 1, 'at': 1, 'ate': 1, 'be': 1, 'black': 1,
           'brown': 1, 'but': 1, 'came': 1, 'did': 1, 'do': 1, 'eat': 1, 'four': 1, 'get': 1, 'good': 1,
           'have': 1, 'he': 1, 'into': 1, 'like': 1, 'must': 1, 'new': 1, 'no': 1, 'now': 1, 'on': 1, 'our': 1,
           'out': 1, 'please': 1, 'pretty': 1, 'ran': 1, 'ride': 1, 'saw': 1, 'say': 1, 'she': 1, 'so': 1,
           'soon': 1, 'that': 1, 'there': 1, 'they': 1, 'this': 1, 'too': 1, 'under': 1, 'want': 1, 'was': 1,
           'well': 1, 'went': 1, 'what': 1, 'white': 1, 'who': 1, 'will': 1, 'with': 1, 'yes': 1, 'after': 1,
           'again': 1, 'an': 1, 'any': 1, 'ask': 1, 'as': 1, 'by': 1, 'could': 1, 'every': 1, 'fly': 1, 'from': 1,
           'give': 1, 'going': 1, 'had': 1, 'has': 1, 'her': 1, 'him': 1, 'his': 1, 'how': 1, 'just': 1, 'know': 1,
           'let': 1, 'live': 1, 'may': 1, 'of': 1, 'old': 1, 'once': 1, 'open': 1, 'over': 1, 'put': 1, 'round': 1,
           'some': 1, 'stop': 1, 'take': 1, 'thank': 1, 'them': 1, 'then': 1, 'think': 1, 'walk': 1, 'were': 1,
           'when': 1, 'always': 1, 'around': 1, 'because': 1, 'been': 1, 'before': 1, 'best': 1, 'both': 1,
           'buy': 1, 'call': 1, 'cold': 1, 'does': 1, "don't": 1, 'fast': 1, 'first': 1, 'five': 1, 'found': 1,
           'gave': 1, 'goes': 1, 'green': 1, 'its': 1, 'made': 1, 'many': 1, 'off': 1, 'or': 1, 'pull': 1,
           'read': 1, 'right': 1, 'sing': 1, 'sit': 1, 'sleep': 1, 'tell': 1, 'their': 1, 'these': 1, 'those': 1,
           'upon': 1, 'us': 1, 'use': 1, 'very': 1, 'wash': 1, 'which': 1, 'why': 1, 'wish': 1, 'work': 1,
           'would': 1, 'write': 1, 'your': 1, 'about': 1, 'better': 1, 'bring': 1, 'carry': 1, 'clean': 1,
           'cut': 1, 'done': 1, 'draw': 1, 'drink': 1, 'eight': 1, 'fall': 1, 'far': 1, 'full': 1, 'got': 1,
           'grow': 1, 'hold': 1, 'hot': 1, 'hurt': 1, 'if': 1, 'keep': 1, 'kind': 1, 'laugh': 1, 'light': 1,
           'long': 1, 'much': 1, 'myself': 1, 'never': 1, 'only': 1, 'own': 1, 'pick': 1, 'seven': 1, 'shall': 1,
           'show': 1, 'six': 1, 'small': 1, 'start': 1, 'ten': 1, 'today': 1, 'together': 1, 'try': 1, 'warm': 1}
    li = li.replace('\n', ' ').replace(':',' ').replace('?',' ').replace('-',' ').replace('.',' ').replace(',',' ').replace('!',' ').lower().split(' ')
    model = collections.defaultdict(lambda: 0)
    for f in li:
        model[f] += 1
    del model['']
    for key in fil.keys():
        if key in model.keys():
            del model[key]
        list1 = sorted(model.items(), key=lambda x: (x[1], x[0]),reverse=True)
    if list1 != []:
        list2 = []
        for i in range(10):
            list2.append(list1[i])
        return list2
    else:
        return []


if __name__ == '__main__':
    pass

