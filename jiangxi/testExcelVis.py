# -*- coding: utf8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']    # 添加汉字/ #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
sales = pd.read_excel('F:/anaconda/a3.xlsx', names=["zaofa1", "zaofa2", "zaofa3", "zaofa4"], header=0)
# 读取文件，并且为列取名字
'''导入行列数据'''
width = sales.zaofa2                           # 作用仅是给横坐标确定位置
height = sales.zaofa4                         # 目标画图点
'''线形样式设置,颜色，各种参数直接在里面改'''
# plt.style.use("dark_background")                                  #设置背景样式
# plt.scatter(width, height)                                        #散点图
plt.plot(width, height, color="r", marker="*")                      # 折线图
# plt.barh(width, height)                                           #水平条形图
# plt.bar(width, height, color="#008080")                           #条形图
'''图例、标题设置'''
plt.title('卢造发 made it!', fontsize=20)
plt.xlabel("时 间", fontsize=15)
plt.ylabel("成绩", fontsize=15, rotation=40)
# group_labels = ["星期一", '二', "三", "四", "五", "星期六", "星期天"]
# 显示特定横线坐标(1)
group_labels = sales["zaofa1"]
plt.xticks(width, group_labels, rotation=-40)
# 显示特定横线坐标(2)依靠width的大小确定横坐标位置
# plt.grid(True)                                       #网格线显示与否
'''添加数字标签'''
for a, b in zip(width, height):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=17)
plt.tight_layout()                                       # 紧凑型输出
savefig("F:/anaconda/a.jpg")                 # 存储图片
