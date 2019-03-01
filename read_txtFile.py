import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

connect = serial.Serial("",9600) # port
fig,axes = plt.subplots(1,1) #產生axes物件
axes.set(title='PM2.5 Conc.') # 設子圖title
def save_data():
        data = connect.readline()
        data = data.decode("utf-8")
        with open("sample.txt","a") as file:
            file.write(data)
while True:
    save_data()
    
    def anima(i):
        graph_data = open("sample.txt",'r').read()
        line_records = graph_data.split("\n")
        line_records.pop()
        line_records = line_records[-6:]
    
        xs = []
        ys =[]
        # line_records = line_records[-5,-1]
        for record in line_records:
        
            if len(record) > 2:
                x,y = record.split(",")
                xs.append(float(x))
                ys.append(float(y))

        axes.clear()
        axes.set_ylim(0,20)
        axes.grid(True)
        axes.plot(xs,ys)

    ani = animation.FuncAnimation(fig,anima, interval = 1000)

    plt.show()