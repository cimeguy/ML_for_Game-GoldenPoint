import numpy as np
from sklearn import  linear_model


def get_player_name():
    name = 'jiangjiaqi'
    return name


def get_number(h_data):
    number=[]
    gold=[]
    x=[]
    sum=0
    for i in h_data:
        number.append(h_data[i])
    b=len(number[0])
    if b==0:
        return (50,51)
    else:
        for i in range(b) :
            for j in range(len(h_data)):
                sum=sum+number[j][i][0]+number[j][i][1]
            g=sum/(2*len(h_data))
            gold.append(float(g))
            sum=0
        for i in range(b):
            x.append([float(i+1)])
        regr = linear_model.LinearRegression()
        regr.fit(x, gold)
        c=np.array([b+1])
        G = regr.predict(c.reshape(-1,1))
        G.tolist()
        if (G>50):
            disturb=0
        else:
            disturb=100
        tub= (G[0],G[0])
        return tub



if __name__ == '__main__':
    history_data = {'Bob': [],
                    'Bart' : [],
                    'Mary' : []}

    print(get_number(history_data))
    print(get_player_name())
