from tkinter import *
# Label Entry Radiobutton Checkbutton Button Text Scrollbar Canvas
root=Tk()
canvas=Canvas(root) #创建canvas画布
canvas.pack(fill=BOTH,expand=1)

#绘制图形：1、填充  2、画线

#画布里边绘制一条线，并且记录下来方便后边用
# line=canvas.create_line(10,10,100,100,fill="red",width=10)
# 四个数值前俩个是起始坐标，后俩个是结束坐标
# print(line)

# line=canvas.create_line(10,10,100,100)
# canvas.itemconfig(line,fill="red",width=10,arrow="first")
#动态修改样式,
# arrow，设置箭头。first:开始；last:结尾，both：俩头。arrowshape=[40 50 30]x填充的长度，y箭头的长度，z箭头的宽度。

# canvas.coords(line,100,0,100,100)#coords修改位置和尺寸
# canvas.create_line((10,10,100,100))#本应该是元组，但是上边那样写也没错

#绘制矩形
# canvas.create_rectangle(100,100,200,200,outline="red",fill="blue",width=10)
#outline边框，fill填充，width边框的宽度。可以为空，但是不代表不存在。

#绘制弧
# canvas.create_arc(0,0,100,100,extent=120,start=10,dash=(1,1))
#还可以加style，设置为PIESLICE, CHORD, or ARC. Default is PIESLICE.
#dash虚线，俩个值代表长度和间距.

#绘制圆
# canvas.create_oval(0,0,100,100)

#绘制三角形
# canvas.create_polygon(10,10,100,10,10,100,outline="red",fill="")

#绘制文字
# canvas.create_text(100,100,text="我是文字")

#把组件以图形的方式放上来，下边是按钮案例。
# btn=Button(canvas,text="我是按钮")
# canvas.create_window(100,100,window=btn)


#python操作图形图像
# tkinter  俩种：
# 1、位图，
#绘制位图
# canvas.create_bitmap(100,100,bitmap="question")
# 'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', and 'warning'.简单的图标
#引入图片只能处理gif格式的,如：
# img=PhotoImage(file="my.gif")
# Label(root,image=img).pack()
# 2、pillow库。处理图形图像的一种方法。



import math
#画多边形方法
def bian(originx,originy,r,num):
    points=[]
    for item in range(0,num):
        angle=360/num*item
        x=math.cos(math.pi/180*angle)*r+originx
        y=math.sin(math.pi/180*angle)*r+originy
        points.append(x)
        points.append(y)
    canvas.create_polygon(points,fill="",outline="red")
bian(100,100,100,5)

#画内角的多边形方法1
def jiao(originx,originy,r,num):
    points=[]
    for item in range(0,num):
        angle=(360/num)*2*item
        x=math.cos(math.pi/180*angle)*r+originx
        y=math.sin(math.pi/180*angle)*r+originy
        points.append(x)
        points.append(y)
    canvas.create_polygon(points,fill="",outline="red")
jiao(100,100,100,5)

#画内角的多边形方法2（优于第一种，第一种只能画奇数的）
比如五角星一共要确定十个点，十个点交叉输出连成线就绘成了五角星。
需要确定外部的五个点和内部的五个点。然后外部点用内部点交叉连接。所以用判断偶数奇数的方式让他们交叉出现。
originx 和 originy 是定义相对于浏览器的位置。
num参数是看要画几边形，五角星就是5.
r1,r2分别是俩个圈即每五个点（五个外部的点、五个内部的点）组成的圆的半径，不用管r1是对应大圈还是小圈。
fill是填充，outline是边框线。
def jiao(originx,originy,num,r1,r2):
    points=[]
    for item in range(0,num*2):
        angle = 360 / (num * 2) * item
        if item%2==0:#如果能被整除获取一种值
            x = math.cos(angle *math.pi / 180) * r1 + originx#math.pi / 180 将度数转化为弧度
            y = math.sin(angle *math.pi / 180) * r1 + originy
        else:#不能获取另外一种，
            x = math.cos(angle *math.pi / 180) * r2 + originx
            y = math.sin(angle *math.pi / 180) * r2 + originy
        points.append(x)
        points.append(y)
    tuxing=canvas.create_polygon(points)
    canvas.itemconfig(tuxing,fill="", outline="red")
jiao(100,100,5,100,40)
root.mainloop()
