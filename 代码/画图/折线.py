# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 11:55:21 2023

@author: Administrator
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot') #设置风格
x = [1,2,3,4,5,6,7,8,9]
y1 = [2,3,4,56,2,5,7,5,3]
y2 = [4,6,7,8,9,1,21,45,6]

plt.figure(figsize = (10,6),dpi = 80) #设置画布
plt.grid() #设置背景有网格
plt.plot(x, y1,'r*-',linewidth=2) #根据坐标画线
plt.plot(x,y2,'b*-',linewidth=2)
plt.xlabel('epoch', size = 15)
plt.ylabel('accracy',size = 15)
plt.legend(['model I','model II']) #加载图例
plt.title("Accuracy")
plt.show()




