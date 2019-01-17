# -*- coding: UTF-8 -*-

import os


def filter_c_file(dir_path):
    cfile = []
    pat = os.listdir(dir_path)
    for file in pat:
        filepath = os.path.join(dir_path, file)
        if os.path.isfile(filepath):
            ext = os.path.splitext(file)[1]
            if ext in [".cpp", ".c"]:
                cfile.append(file)
    for file in cfile:
        try:
            f = open(dir_path+'/'+file, 'r',encoding='utf8' )
            st = f.readlines()
            f.close()
            for i in range(len(st)):
                for x in range(len(st)):
                    end = st[x].find('}')
                    if end != -1:
                        for z in range(len(st[x:])):
                            while(z+2)<len(st[x:]):
                                st[z+x+2] = ''
                                break
                if st[i].find('#') == 0:
                    st[i] = '\t'
                flag1 = st[i].find('//')
                flag2 = st[i].find('(')
                flag3 = st[i].find(')')
                if flag1 != -1:
                    if flag1 >= 1:
                        if (flag2 != -1) and (flag2 < flag1) and (flag3 > flag1):
                            pass
                        else:
                            st[i] = st[i][:flag1]
                    elif flag1 == 0:
                        st[i] = '\t'
                flag = st[i].find('/*')
                if flag != -1:
                    block = 0
                    j1 = 0
                    for j in range(len(st[i:])):
                        rflag1 = st[i+j].find('*/')
                        if rflag1 != -1:
                            block = 1
                            j1 = j+i
                            if st[j1] !='':
                                st[j1] = ''+st[j1][rflag1+2:]
                            else:
                                st[j1]
                    if block:
                        st[i] = st[i][:flag]
                        for n in range(i+1,j1):
                            st[n] = '\t'
                    if flag>1:
                        rflag = st[i].find('*/')
                        if rflag != -1:
                            st[i] = st[i][:flag] + st[i][rflag:]
                    elif flag == 0:
                        st[i] = '\t'
                    elif flag and rflag == -1:
                        st[i] = st[i][:flag]
                if st[i] != '':
                    st[i] = st[i].replace('\t', '').replace('\n', '').replace(' ','')
            name = file.replace('.cpp', '.txt')
            text = open(dir_path+'/'+name, 'w')
            for y in range(len(st)):
                text.write(st[y])
            text.close()
        except:
            print('failed')


if __name__ == '__main__':
    pass
