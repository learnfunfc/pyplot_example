
import matplotlib.animation as animation
import matplotlib.pyplot as pt
from matplotlib import style
# file_data = open("sample.txt",'r')
# graph_data = file_data.read()
# file_data.close()
# lines= graph_data.split("\n")
# print(lines)

style.use('fivethirtyeight')

fig = pt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.set_title("temp")

def animations(i):
    graph_data = open("sample.txt","r").read()
    
    lines= graph_data.split("\n")
   
    xs =[]
    ys=[]
    new_line = lines[-5:-1]
    for line in new_line:
        if len(line)>1:
            x,y = line.split(',')
            xs.append(x)
            ys.append(y)


    ax1.clear()
    
    ax1.plot(xs,ys, label="A")

ani= animation.FuncAnimation(fig,animations,interval=1000)
pt.show()
