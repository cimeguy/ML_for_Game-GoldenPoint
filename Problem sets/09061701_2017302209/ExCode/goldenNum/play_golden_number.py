#!/usr/bin/python
# -*- coding:UTF-8 -*-


import matplotlib.pyplot as plt
import matplotlib
from numpy import *
import os
import copy


def get_client_files(source_dir):
    fp = os.listdir(source_dir)
    _file_list = []
    for item in fp:
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1]
            if ext in [".py"]:
                _file_list.append(item_path)
    return _file_list


# 在上图显示黄金点变化情况，点线图
# num：列表，包含了从第一轮到当前所有的黄金点
def plot_golden_num(ax, nums):
    x = range(len(nums))
    ax.set_xlim(auto=True, left=0, right = len(nums))
    ax.set_ylim(auto=True, bottom=0, top = max(nums))
    ax.get_lines()[0].set_xdata(x)
    ax.get_lines()[0].set_ydata(nums)


# 在下图显示各队排名变化情况，直方图
# num：字典，key为队名，value为得分，如：{'bob': -5, '我爱Python': 3, 'Alice': 6}
def plot_score(ax, score):
    ax.cla()
    ax.set_ylim(auto=True, bottom=0, top = max(score.values()))
    y_pos = range(len(score.keys()))
    bh = ax.barh(y_pos, list(score.values()),align='center', color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(score.keys())

    for b in bh:
        w = b.get_width()
        ax.text(b.get_x()/2 + w/2 , b.get_y() + b.get_height()/2, '%d' % int(w), ha='center', va='bottom')


# 准备画图
def plot_gnum_init():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    fig1, ax1 = plt.subplots()
    ax1.set_xlabel('轮数')
    ax1.set_ylabel('黄金点数')
    ax1.set_title('黄金点变化曲线')
    ax1.grid(True)
    ax1.set_xlim(auto=False, left=0, right = 400)
    ax1.set_ylim(auto=False, bottom=0, top = 100)
    ax1.plot([0,0],[0,0],'-g',marker='*')

    plt.ion()
    plt.show()

    return ax1


# 准备画图
def plot_barh_init(names):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    fig2, ax2 = plt.subplots()
    ax2.set_xlabel('总分')
    ax2.set_ylabel('玩家')
    ax2.set_title('玩家得分图')
    ax2.set_xlim(auto=False, left=0, right = 100)
    ax2.set_ylim(auto=False, bottom=0, top = len(names))

    y_pos = range(len(names))
    sc = zeros(len(names))

    bh = ax2.barh(y_pos, sc,align='center', color='green', ecolor='black')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(names)

    for b in bh:
        w = b.get_width()
        ax2.text(w + 1, b.get_y() + b.get_height()/2, '%d' % int(w), ha='center', va='bottom')

    plt.ion()
    plt.show()

    return ax2


if __name__ == '__main__':
    print("准备环境 ......")
    path = ".\clients"
    _client_files = get_client_files(path)

    _clients_dict = dict()
    for item in _client_files:
        _client_str = open(item, "r", encoding="utf8").read()
        con = {}
        exec(_client_str, con)

        client_exec = dict()  # 单个客户端环境
        client_exec["file_name"] = item  # 客户端文件名
        client_exec["get_number"] = con["get_number"]  # 客户端玩家的生成函数
        client_exec["h_numbers"] = []  # 记录每次提交的黄金点二元组
        client_exec["score"] = 0  # 积分
        player_name = con["get_player_name"]()

        _clients_dict[player_name] = client_exec

    # todo: 避免队伍名字重复
    print("欢迎参赛选手：")
    index = 1
    for name in _clients_dict.keys():
        print(str(index) + "." + name)
        index += 1

    print("准备开始比赛，共400轮 ......")
    ax1 = plot_gnum_init()
    ax2 = plot_barh_init(_clients_dict.keys())

    plt.pause(6)

    g_num_list = []
    for index in range(1,400):
        # 获取历史数据
        h_data = dict()
        for name, client in _clients_dict.items():
            h = client["h_numbers"]
            if name not in h_data:
                h_data[name] = copy.deepcopy(h)

        # 从每个玩家获取数据
        c_data = dict()
        for name, client in _clients_dict.items():
            fun = client["get_number"]
            n1, n2 = fun(h_data)
            n1 = round(n1,10)
            n2 = round(n2,10)

            if n1 >= 100:
                n1 = 99.9999999999
            if n2 >= 100:
                n2 = 99.9999999999

            if n1 <= 0:
                n1 = 0.0000000001
            if n2 <= 0:
                n2 = 0.0000000001

            client["h_numbers"].append((n1, n2))
            c_data[name] = (n1, n2)

        # 计算本轮黄金点数
        sum_num = 0
        for name, client in _clients_dict.items():
            n1, n2 = client["h_numbers"][-1]
            sum_num += (n1 + n2)

        g_num = round(0.618 * sum_num/len(_clients_dict),10)
        g_num_list.append(g_num)

        # 确定最近距离和最远距离
        abs_dis = []
        for name, client in _clients_dict.items():
            n1, n2 = client["h_numbers"][-1]
            abs_dis.append(round(abs(n1-g_num),10))
            abs_dis.append(round(abs(n2-g_num),10))

        max_dis = max(abs_dis)
        min_dis = min(abs_dis)

        # 根据最大最小距离记分
        max_count = []
        min_count = []
        score = dict()
        for name, client in _clients_dict.items():
            n1, n2 = client["h_numbers"][-1]
            abs_dis1 = round(abs(n1-g_num),10)
            abs_dis2 = round(abs(n2-g_num),10)
            if max_dis == abs_dis1 or max_dis == abs_dis2:
                client["score"] -= 2
                max_count.append((name,max_dis))

            if min_dis == abs_dis1 or min_dis == abs_dis2:
                client["score"] += len(_clients_dict)
                min_count.append((name,min_dis))

            score[name] = client["score"]

        print("score :" + str(score))
        print("G_Num = {g_num}, max_dis: {max}, min_dis: {min}, dict: {d}".format(g_num = g_num, max = max_count, min = min_count, d = c_data))

        # 绘图： 黄金点变化情况(点线图)；排名（直方图）；
        plot_golden_num(ax1, g_num_list)
        plot_score(ax2, score)
        plt.draw()
        plt.pause(0.1)

    os.system("pause")






