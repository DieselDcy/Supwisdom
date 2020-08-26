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


# 江西省各高校按教学类型分类的各项指标均值：
def Rate_stutea(data, col):
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    t = 0
    for n in range(0, data.shape[0]):
        # print(type(data[n, 13]))
        if not(math.isnan(data[n, col])):
            t = t+1
    new_data = np.array([['综合']*t, [10000.00]*t])
    # print(new_data[0, 3])
    for n in range(0, data.shape[0]):
        # print(type(data[n, 13]))
        if not(math.isnan(data[n, col])):
            # print(data[n, :])
            new_data[0, i] = data[n, 3]
            new_data[1, i] = data[n, col]
            i += 1
    # print(new_data)
    new_data = new_data.T
    # print(type(data[18, 13]))
    i = 0
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print(new_data)
    for x in new_data[:, 0]:
        if x == '财经':
            sum[0] = sum[0] + float(new_data[i, 1])
            i += 1
            a[0] += 1
        elif x == '理工':
            sum[1] = sum[1] + float(new_data[i, 1])
            i += 1
            a[1] += 1
        elif x == '农业':
            # print(data[i, 13])
            sum[2] = sum[2] + float(new_data[i, 1])
            i += 1
            a[2] += 1
        elif x == '师范':
            sum[3] = sum[3] + float(new_data[i, 1])
            i += 1
            a[3] += 1
        elif x == '医药':
            sum[4] = sum[4] + float(new_data[i, 1])
            i += 1
            a[4] += 1
        elif x == '艺术':
            sum[5] = sum[5] + float(new_data[i, 1])
            i += 1
            a[5] += 1
        elif x == '语言':
            sum[6] = sum[6] + float(new_data[i, 1])
            i += 1
            a[6] += 1
        elif x == '政法':
            sum[7] = sum[7] + float(new_data[i, 1])
            i += 1
            a[7] += 1
        elif x == '综合':
            sum[8] = sum[8] + float(new_data[i, 1])
            i += 1
            a[8] += 1
    x1 = ['财经', '理工', '农业', '师范', '医药', '艺术', '政法', '综合']
    y1 = [sum[0]/(a[0]+0.01), sum[1]/(a[1]+0.01), sum[2]/(a[2]+0.01),
            sum[3]/(a[3]+0.01), sum[4]/(a[4]+0.01), sum[5]/(a[5]+0.01),
            sum[7]/(a[7]+0.01), sum[8]/(a[8]+0.01)]

    # 江西省各类别高校全日制在校本科生数情况
    if col == 5:
        print('江西省各类别高校全日制在校本科生数情况')
        print('财经：', sum[0], sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校全日制在校本科生数情况'
    # 江西省各类别高校专任教师数情况
    if col == 8:
        print('江西省各类别高校专任教师数情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校专任教师数情况'
    # 江西省各类别高校折合教师数
    if col == 10:
        print('江西省各类别高校折合教师数')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校折合教师数'
    # 江西省各类别高校全校本科专业数情况
    if col == 12:
        print('江西省各类别高校全校本科专业数情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校全校本科专业数情况'
    # 江西省各类别高校生师比：
    if col == 13:
        print('江西省各类别高校生师比')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校生师比情况'
    # 江西省各类别高校生均教学科研仪器设备值情况
    if col == 14:
        print('江西省各类别高校生均教学科研仪器设备值情况')
        print('财经：', sum[0]/(a[0]+0.01), '万元')
        print('理工：', sum[1]/(a[1]+0.01), '万元')
        print('农业：', sum[2]/(a[2]+0.01), '万元')
        print('师范：', sum[3]/(a[3]+0.01), '万元')
        print('医药：', sum[4]/(a[4]+0.01), '万元')
        print('艺术：', sum[5]/(a[5]+0.01), '万元')
        print('语言：', sum[6]/(a[6]+0.01), '万元')
        print('政法：', sum[7]/(a[7]+0.01), '万元')
        print('综合：', sum[8]/(a[8]+0.01), '万元')
        Gtitle = '江西省各类别高校生均教学科研仪器设备值情况'
    # 江西省各类别高校生均图书情况
    if col == 16:
        print('江西省各类别高校生均图书情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校生均图书情况'
    # 江西省各类别高校生均教学行政用房情况
    if col == 18:
        print('江西省各类别高校生均教学行政用房情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校生均教学行政用房情况'
    # 江西省各类别高校生均本科教学日常运行支出(元)情况
    if col == 19:
        print('江西省各类别高校生均本科教学日常运行支出(元)情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校生均本科教学日常运行支出(元)情况'
    # 江西省各类别高校全校开设课程总门数情况
    if col == 23:
        print('江西省各类别高校全校开设课程总门数情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校全校开设课程总门数情况'
    # 江西省各类别高校主讲本科课程的教授占教授总数的比例情况
    if col == 26:
        print('江西省各类别高校主讲本科课程的教授占教授总数的比例情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校主讲本科课程的教授占教授总数的比例情况'
    # 江西省各类别高校应届本科生毕业率情况
    if col == 28:
        print('江西省各类别高校应届本科生毕业率情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校应届本科生毕业率情况'
    # 江西省各类别高校应届本科生初次就业率情况
    if col == 30:
        print('江西省各类别高校应届本科生初次就业率情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校应届本科生初次就业率情况'
    # 江西省各类别高校体质测试达标率情况
    if col == 31:
        print('江西省各类别高校体质测试达标率情况')
        print('财经：', sum[0]/(a[0]+0.01))
        print('理工：', sum[1]/(a[1]+0.01))
        print('农业：', sum[2]/(a[2]+0.01))
        print('师范：', sum[3]/(a[3]+0.01))
        print('医药：', sum[4]/(a[4]+0.01))
        print('艺术：', sum[5]/(a[5]+0.01))
        print('语言：', sum[6]/(a[6]+0.01))
        print('政法：', sum[7]/(a[7]+0.01))
        print('综合：', sum[8]/(a[8]+0.01))
        Gtitle = '江西省各类别高校体质测试达标率情况'

    histogram(x1, y1, Gtitle)


def histogram(x1, y1, Gtitle):
    plt.bar(x1, y1, color='b')
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
