# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt  #引入库matplotlib.pyplot并命名为plt方便调用
import numpy as np #引入库numpy并命名为np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100) #定义横坐标
y = np.sin(x) #定义原始信号sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)  #绘制多图，指一行有两列两个子图，这一图显示在第一列
plt.title(r'$f(x)=sin(x)$') #显示图形标题 f(x)=sin(x)
plt.plot(x, y) #plt.plot()函数用于画图 它可以绘制点和线，以x为横轴，以y为纵轴绘制图像
#plt.show()

x1 = [t*0.375*np.pi for t in x] #定义y1中的参数 记3πt/8
y1 = np.sin(x1)#定义信号y=sin(3πt/8)
plt.subplot(1,2,2) #绘制多图，指一行有两列两个子图，这一图显示在第二列
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #显示图形标题f(x)=sin(wx),w=3π/8
plt.plot(x, y1)#plt.plot()函数用于画图 它可以绘制点和线，以x为横轴，以y1为纵轴绘制图像
plt.show() #将图像显示