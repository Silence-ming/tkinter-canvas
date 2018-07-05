from tkinter import *
from tkinter import colorchooser
import math
from tkinter import simpledialog
root=Tk()
root.title('画图板')
#设置画布
canvas=Canvas(root)
canvas.pack(fill=BOTH,expand=1)
#用对象的方式写画布，写方法。
#在绘制一个图形的逻辑：按下<B1-Motion>，移动，抬起<ButtonRelease-1>。
class shape:
    def __init__(self,canvas): #初始化
        self.canvas=canvas
        self.bordercolor="#000"
        self.style="outline"
        self.color="#000"
        self.width=1
        self.x=0 #起始位置
        self.y=0
        self.movex = 0 #结束位置
        self.movey = 0
        self.current=0
        self.type="line"
        self.num=5 #边数/角数
        self.arcStyle=ARC
        self.extent=120
        self.flag=False
    def draw(self):
        self.canvas.bind("<Button-1>",self.down)
    def down(self,event):
        self.x=(event.x)  #鼠标按下记录位置
        self.y=(event.y)
        self.canvas.bind("<B1-Motion>",self.move)
        self.canvas.bind("<ButtonRelease-1>", self.up)
    def move(self,event):
        if self.type !="pen" and self.flag==False:#如果不是钢笔绘图需要删除之前画的，可以尝试把此处俩行注释，看看效果。
            self.canvas.delete(self.current)
        self.movex=(event.x) #移动记录位置，因为位置一直在变化需要删除之前的。直到鼠标抬起。
        self.movey=(event.y)
        getattr(self,self.type)()#相当于self.(self.type);getattr函数可以将函数名当做变量处理，不同情况调用不同函数
        self.setStyle()#函数调用下边写了setStyle函数，设置属性用。比如线的颜色，矩形圆等的填充色，宽度等。
    def setStyle(self):
        self.canvas.itemconfig(self.current,width=self.width)
        if self.style=="outline":
            if self.type=="pen" or self.type=="line":
                self.canvas.itemconfig(self.current,fill=self.bordercolor)
            else:
                self.canvas.itemconfig(self.current,fill="",outline=self.bordercolor)
        elif self.style=='fill':
            try:
                self.canvas.itemconfig(self.current,fill=self.color,outline='')
            except:
                pass
        elif self.style=='both':
            try:
                self.canvas.itemconfig(self.current,fill=self.color,outline=self.bordercolor)
            except:
                pass
    def up(self,event):#鼠标抬起，注销移动和抬起事件。
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.current = 0#此处是为了让画线重新开始。
    def line(self):#里边参数为其实坐标和移动最后留下的坐标
        self.current = self.canvas.create_line(self.x, self.y, self.movex, self.movey)
    def rect(self):
        self.current = self.canvas.create_rectangle(self.x, self.y, self.movex, self.movey)
    def arc(self):
        self.current=canvas.create_arc(self.x, self.y, self.movex, self.movey,extent=self.extent,style=self.arcStyle)
    def pen(self):#钢笔或者铅笔工具的不同是需要将上一次画线记录的末尾值变为下一次初始值，这样才能连续画线。呈现随意画线。不同之处在于他不用删除上一次移动记录的位置。方法在move有判定。
        self.current=canvas.create_line(self.x,self.y,self.movex,self.movey)
        self.x=self.movex
        self.y=self.movey
    def circle(self):
        self.current=self.canvas.create_oval(self.x,self.y,self.movex,self.movey)
    def bian(self):
        originx=self.x
        originy=self.y
        num=self.num
        r=math.sqrt((self.movex-self.x)*(self.movex-self.x)+(self.movey-self.y)*(self.movey-self.y))
        points = []
        for item in range(0,num):
            angle=360/num*item
            x=math.cos(math.pi/180*angle)*r+originx
            y=math.sin(math.pi/180*angle)*r+originy
            points.append(x)
            points.append(y)
        self.current=canvas.create_polygon(points)
    def jiao(self):
        originx = self.x
        originy = self.y
        num = self.num
        r1 = math.sqrt((self.movex - self.x) * (self.movex - self.x) + (self.movey - self.y) * (self.movey - self.y))
        r2=r1/2
        points = []
        for item in range(0, num * 2):
            angle = 360 / (num * 2) * item
            if item % 2 == 0:  # 如果能被整除获取一种值
                x = math.cos(angle * math.pi / 180) * r1 + originx  # math.pi / 180 将度数转化为弧度
                y = math.sin(angle * math.pi / 180) * r1 + originy
            else:  # 不能获取另外一种，
                x = math.cos(angle * math.pi / 180) * r2 + originx
                y = math.sin(angle * math.pi / 180) * r2 + originy
            points.append(x)
            points.append(y)
        self.current = canvas.create_polygon(points)

obj=shape(canvas)#对象
obj1=shape(canvas)
#建一个菜单，实现右击然后点对应的选项调用对应的函数实现对应的方法。
main=Menu(root,tearoff=0)#主菜单
tuxing=Menu(main,tearoff=0)#图形栏
arcMenu=Menu(tuxing,tearoff=0)#圆弧子菜单
style=Menu(main,tearoff=0)#样式修改栏
fill=Menu(main,tearoff=0)#填充还是描边
colors=Menu(main,tearoff=0)
delete=Menu(main,tearoff=0)
#图形
def arc(type):
    obj.extent = int(simpledialog.askstring(title='提示框', prompt='请输入角度'))
    obj.type = "arc"
    obj.arcStyle = type
    obj.draw()
def shapeType(types):
    obj.type = types
    obj.draw()
def many(type):
    obj.num = int(simpledialog.askstring(title='提示框', prompt='请输入边数'))
    obj.type = type
    obj.draw()
tuxing.add_command(label="直线",command=lambda :shapeType('line'))
tuxing.add_command(label="钢笔",command=lambda :shapeType('pen'))
tuxing.add_separator()

tuxing.add_command(label="矩形",command=lambda :shapeType('rect'))
tuxing.add_command(label="圆",command=lambda :shapeType('circle'))
tuxing.add_separator()

tuxing.add_command(label="多边形",command=lambda :many('bian'))
tuxing.add_command(label="多角形",command=lambda :many('jiao'))

arcMenu.add_command(label="PIESLICE",command=lambda :arc(PIESLICE))
arcMenu.add_command(label="CHORD",command=lambda :arc(CHORD))
arcMenu.add_command(label="ARC",command=lambda :arc(ARC))

#线宽:
def width():
    obj.width=int(simpledialog.askstring(title='提示框',prompt='请输入线宽'))
def default(num):
    obj.width=num
style.add_command(label='1像素',command=lambda :default('1'))
style.add_command(label='2像素',command=lambda :default('2'))
style.add_command(label='3像素',command=lambda :default('3'))
style.add_command(label='自定义',command=width)
#填充与描边
def fillStyle(type):
    obj.style=type
fill.add_command(label='outline',command=lambda :fillStyle('outline'))
fill.add_command(label='fill',command=lambda :fillStyle('fill'))
fill.add_command(label='both',command=lambda :fillStyle('both'))

#颜色
def color(type):
    result = colorchooser.askcolor()[1]
    if type=='outline':
        obj.bordercolor = result
    elif type=='fill':
        obj.color=result
colors.add_command(label='描边色', command=lambda: color('outline'))
colors.add_command(label='填充色', command=lambda: color('fill'))

#橡皮檫
def dels():
    obj1.type = 'circle'
    obj1.style = 'fill'
    obj1.color = "#F0F0F0"
    obj1.flag=True
    obj1.draw()
delete.add_command(label='擦除',command=dels)

tuxing.add_cascade(label='圆弧',menu=arcMenu)
main.add_cascade(label='图形',menu=tuxing)
main.add_cascade(label='线宽',menu=style)
main.add_cascade(label='填充与描边',menu=fill)
main.add_cascade(label='颜色',menu=colors)
main.add_cascade(label='橡皮檫',menu=delete)
def pop(event):#让菜单对应右击的位置出现。
    main.post(event.x_root,event.y_root)
root.bind("<Button-3>",pop)
root['menu']=main
root.mainloop()