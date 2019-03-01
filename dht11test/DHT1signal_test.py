import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import time

port = "com9"
interval_time = 3 # 設定每三秒擷取一次訊號
connect = serial.Serial(port,9600,timeout=1.5) # port
fig,axes = plt.subplots(1,1) #產生axes物件
axes.set(title='Temperture') # 設子圖title
 
ys=[]

     
def anima(i):
        global ys
        data = connect.readline()
        data = data.decode("utf-8")
        if len(data)>3: 
                data = data.rstrip("\r\n")
                data = float(data)
                date_hr = time.strftime("%H:%M:%S")
                print(date_hr,data)
                ys.append(data)
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
        axes.set_ylim(0,40)
        axes.grid(True)
        #axes.plot(xs,ys)
        axes.plot(ys)
        time.sleep(interval_time)

ani = animation.FuncAnimation(fig,anima, interval = 1000)

plt.show()
     
    
