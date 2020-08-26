import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pygal # Pygal生成可缩略的矢量图文件

# 加入中文显示
import  matplotlib.font_manager as fm
# 解决中文乱码，本案例使用宋体字
myfont = fm.FontProperties(fname=r"C:\\Windows\\Fonts\\simsun.ttc")


def histogram(xvalues, yvalues):
    # 绘制直方图
    hist = pygal.HorizontalBar()

    # 设置散点图标题和横纵坐标标题
    hist.title = '江西省各学校全日制在校生本科生数对比'
    hist.x_title = '全日制在校生本科生数'
    hist.y_title = ''

    # 绘图,设置图形大小
    fig = plt.figure(dpi=100, figsize=(18, 6))

    # 事件的结果
    hist.x_labels = xvalues

    # 事件的统计频率
    hist.add('', yvalues)

    # 保存文件路径
    hist.render_to_file('die_visual.svg')


if __name__ == '__main__':
    path = r'C:\Users\Chengyu.Dean\Desktop\树维\江西省挖煤\【2019】本科教学质量报告核心数据提取(25)(3).xlsx'
    # df = pd.read_excel(path, sheet_name='江西', usecols=[0, 5])
    # xvalues = list(range(1, 100))  # 校正坐标点，即横坐标值列表
    # yvalues = [x**2 for x in xvalues]  # 纵坐标值列表
    x = pd.read_excel(path, sheet_name='江西', usecols=[0])
    y = pd.read_excel(path, sheet_name='江西', usecols=[5])
    x_result = x['学校名称'].values.tolist()  # 将DataFrame, Series转化为list
    y_frequencies = y['全日制在校本科生数'].values.tolist()
    # print(y)
    histogram(x_result, y_frequencies)
