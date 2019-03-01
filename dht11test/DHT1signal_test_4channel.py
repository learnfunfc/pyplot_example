import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial


connect = serial.Serial("com17",9600,timeout=1.5) # port
fig,axes= plt.subplots(1,1) #產生axes物件


ysA=[]
ysB=[]
ysC=[]
ysD=[]


# while True:
#         data = connect.readline()
        
#         # print(data)
#         data = data.decode("utf-8")
#         if len(data)>3: 
#                 data = data.rstrip("\r\n")
#                 print(float(data))

     
def anima(i):
        
        global ysA
        data = connect.readline()
        data = data.decode("utf-8")
        if len(data)>3: 
                data = data.rstrip("\r\n")
                data_list = data.split()
                print(data_list)
                ysA.append(float(data_list[0]))
                ysB.append(float(data_list[1]))
                ysC.append(float(data_list[2]))
                ysD.append(float(data_list[3]))
                # with open("sample.txt","a") as file:
                #     file.write(data)
                                
                # graph_data = open("sample.txt",'r').read()
                # line_records = graph_data.split("\n")
                # line_records.pop()
                # line_records = line_records[-6:]
        
                # xs = []
                
                # line_records = line_records[-5,-1]
                # for record in line_records:
                
                #     if len(record) > 2:
                #         x,y = record.split(",")
                #         #xs.append(float(x))
                #         ys.append(float(y))
        
        axes.clear()
        axes.set_title('Temperture') # 設子圖title !!!!!!!!!
        axes.set_ylim(0,40)
        axes.grid(True)
        
        axes.plot(ysA, label="A channel")
        axes.plot(ysB, label="B channel")
        axes.plot(ysC, label="C channel")
        axes.plot(ysD, label="D chaneel")
        axes.legend() # 產生figure legend(圖例)


ani = animation.FuncAnimation(fig,anima, interval = 1000)

plt.show()
     
    
