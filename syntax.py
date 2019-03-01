

import matplotlib.pyplot as plt
fig1 = plt.figure(1,figsize=(8,8)) # 產生名為figure 1的圖表視窗
fig1.subplots(2,2) # 在figure 1中產生 2x2的次圖表

plt.subplot(2,2,2) # focus on the second subplot
plt.title("demo2")
plt.axis([0,10,0,50]) # [xmin,xmax,ymin,ymax]
plt.plot([1,2,3,4,5,6],[1,8,5,10,20,12],lw=1) # (x-axis,y-axis, line-width)
plt.grid(True) # show grid line

# 修改第一個 subplot
plt.subplot(2,2,1) # focus on the first subplot of figure1 
plt.title("demo1") # the title of the first subplot is demo1
plt.xlabel('Time', fontsize=12, color='red') # 設定x軸的標籤
plt.ylabel('Conc.', fontsize=12, color='blue') # 設定x軸的標籤



plt.axis([-10,10,0,50]) # [xmin,xmax,ymin,ymax]
# plt.xlim(-10,10) # 設定 x軸範圍
plt.yscale('linear') # 設定y座標以線性標示
# plt.yscale('log')
# plt.yscale('symlog', linthreshy=0.0)
# plt.yscale('logit')
plt.scatter([1,2,3,4,5,6],[20,10,5,12,15,12]) # (x-axis,y-axis) scatter plot


plt.show()