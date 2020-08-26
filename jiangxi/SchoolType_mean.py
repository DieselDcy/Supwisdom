import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
# 加入中文显示
import matplotlib.font_manager as fm
# 解决中文乱码，本案例使用宋体字
myfont = fm.FontProperties(fname=r"C:\\Windows\\Fonts\\simsun.ttc")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 江西省各高校按学校类别分类的各项指标均值：
def Rate_stutea(data, col):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    i = 0
    t = 0
    # x = data.shape(0)*[]
    for n in range(0, data.shape[0]):
        # print(type(data[n, 13]))
        if not(math.isnan(data[n, col])):
            t = t+1
    new_data = np.array([['普通本科']*t, [0]*t])
    # print(new_data[0, 3])
    for n in range(0, data.shape[0]):
        # print(type(data[n, 13]))
        if not(math.isnan(data[n, col])):
            # print(data[n, :])
            new_data[0, i] = data[n, 2]
            new_data[1, i] = data[n, col]
            i += 1
    new_data = new_data.T
    # print(type(data[18, 13]))
    i = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    for x in new_data[:, 0]:
        if x == '985':
            sum1 = sum1 + new_data[i, 1]
            i += 1
            a1 += 1
        elif x == '211':
            sum2 = sum2 + float(new_data[i, 1])
            i += 1
            a2 += 1
        elif x == '普通本科':
            # print(data[i, 13])
            sum3 = sum3 + float(new_data[i, 1])
            i += 1
            a3 += 1
        elif x == '独立学院':
            sum4 = sum4 + float(new_data[i, 1])
            i += 1
            a4 += 1

    x1 = ['985院校', '211院校', '普通本科院校', '独立学院']
    y1 = [sum1/(a1+0.01), sum2/(a2+0.01), sum3/(a3+0.01), sum4/(a4+0.01)]

    # 江西省各类别高校全日制在校本科生数情况
    if col == 5:
        print('江西省各类别高校全日制在校本科生数情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校全日制在校本科生数情况'
    # 江西省各类别高校专任教师数情况
    if col == 8:
        print('江西省各类别高校专任教师数情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校专任教师数情况'
    # 江西省各类别高校折合教师数
    if col == 10:
        print('江西省各类别高校折合教师数')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校折合教师数'
    # 江西省各类别高校全校本科专业数情况
    if col == 12:
        print('江西省各类别高校全校本科专业数情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校全校本科专业数情况'
    # 江西省各类别高校生师比：
    if col == 13:
        print('江西省各类别高校生师比')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校生师比情况'
    # 江西省各类别高校生均教学科研仪器设备值情况
    if col == 14:
        print('江西省各类别高校生均教学科研仪器设备值情况')
        print('985院校：', sum1/(a1+0.01), '万元')
        print('211院校：', sum2/(a2+0.01), '万元')
        print('普通本科院校：', sum3/(a3+0.01), '万元')
        print('独立学院：', sum4/(a4+0.01), '万元')
        Gtitle = '江西省各类别高校生均教学科研仪器设备值情况'
    # 江西省各类别高校生均图书情况
    if col == 16:
        print('江西省各类别高校生均图书情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校生均图书情况'
    # 江西省各类别高校生均教学行政用房情况
    if col == 18:
        print('江西省各类别高校生均教学行政用房情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校生均教学行政用房情况'
    # 江西省各类别高校生均本科教学日常运行支出(元)情况
    if col == 19:
        print('江西省各类别高校生均本科教学日常运行支出(元)情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校生均本科教学日常运行支出(元)情况'
    # 江西省各类别高校全校开设课程总门数情况
    if col == 23:
        print('江西省各类别高校全校开设课程总门数情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校全校开设课程总门数情况'
    # 江西省各类别高校主讲本科课程的教授占教授总数的比例情况
    if col == 26:
        print('江西省各类别高校主讲本科课程的教授占教授总数的比例情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校主讲本科课程的教授占教授总数的比例情况'
    # 江西省各类别高校应届本科生毕业率情况
    if col == 28:
        print('江西省各类别高校应届本科生毕业率情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校应届本科生毕业率情况'
    # 江西省各类别高校应届本科生初次就业率情况
    if col == 30:
        print('江西省各类别高校应届本科生初次就业率情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校应届本科生初次就业率情况'
    # 江西省各类别高校体质测试达标率情况
    if col == 31:
        print('江西省各类别高校体质测试达标率情况')
        print('985院校：', sum1/(a1+0.01))
        print('211院校：', sum2/(a2+0.01))
        print('普通本科院校：', sum3/(a3+0.01))
        print('独立学院：', sum4/(a4+0.01))
        Gtitle = '江西省各类别高校体质测试达标率情况'

    histogram(x1, y1, Gtitle)


def histogram(x1, y1, Gtitle):
    plt.bar(x1, y1, color='rgby')
    plt.title(Gtitle)
    plt.xlabel('高校类别')
    plt.ylabel('均值水平')
    plt.show()


if __name__ == '__main__':
    path = input('请输入文件路径：')
    if int(path) < 1:
        path = r'C:\Users\Chengyu.Dean\Desktop\树维\江西省挖煤\【2019】本科教学质量报告核心数据提取(25)(3).xlsx'
    sh_data = pd.read_excel(path, sheet_name='江西')
    # print(sh_data.iloc[0:1, :2])
    # print(sh_data.iat[0, 1])
    # print(sh_data.loc[sh_data.index[0], '学校类别'])
    # 返回二维数组
    data = sh_data.values
    n = input('请输入所需分析指标在表格中的列序：')
    Rate_stutea(data, int(n)-1)
