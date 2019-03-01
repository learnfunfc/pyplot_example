import matplotlib.pyplot as plt
#figure 中只有一個subplot情況
fig2,axes1 = plt.subplots(1,1) #產生axes物件
axes1.set(title='Upper Left')#第一个坐标轴

#產生四個子圖
fig,axes2 = plt.subplots(nrows=2, ncols=2) #產生axes物件
axes2[0,0].set(title='Upper Left')#第一个坐标轴
axes2[0,1].set(title='Upper Right')#右1
axes2[1,0].set(title='Lower Left')#左下1
axes2[1,1].set(title='Lower Right')#右下1

#axes2[0,0].set_title("new title") # axes物件設定title
axes2[0,0].plot([1,2,3,4,5,6],[1,8,5,10,20,12],lw=1,label="A")


plt.show()
