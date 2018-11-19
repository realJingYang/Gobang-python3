from tkinter.messagebox import *
from tkinter import*
from random import*
import winsound
import os

#声明全局变量开始
global   canvas
global   back_x,back_y,last
global   qipan
qipan=   [[2 for i in range(16)]for i in range(16)]                  #2表示空，0表示红棋，1表示绿棋
col=     ['红','绿']
global   index                                                       #创建落子计数变量
index=   0
global var_top
global hui
hui=0
#声明全局变量结束

long=    100
dtmf=    [697,770,852,941,1209,1336,1477,1633]
fequency=[440,494,554,587,659,740,831,880]

winsound.PlaySound("1.wav",0)                                 #播放启动音效


#函数开始
def another_color(color):
    return 1-color

def is_win(color):                                                   #判赢函数
    global qipan
    global index
    global canvas
    kuan=16
    i=j=0
#横排
    for i in range(kuan):
        for j in range(kuan-4):
            if(qipan[i][j]==color and qipan[i][j+1]==color and qipan[i][j+2]==color and qipan[i][j+3]==color and qipan[i][j+4]==color):
                return 1
#竖排
    for i in range(kuan-4):
        for j in range (kuan):
            if(qipan[i][j]==color and qipan[i+1][j]==color and qipan[i+2][j]==color and qipan[i+3][j]==color and qipan[i+4][j]==color):
                return 1
#副对角线
    for i in range(kuan-4):
        for j in range(4,kuan):
            if(qipan[i][j]==color and qipan[i+1][j-1]==color and qipan[i+2][j-2]==color and qipan[i+3][j-3]==color and qipan[i+4][j-4]==color):
                return 1
#主对角线
    for i in range(kuan-4):
        for j in range(kuan-4):
            if(qipan[i][j]==color and qipan[i+1][j+1]==color and qipan[i+2][j+2]==color and qipan[i+3][j+3]==color and qipan[i+4][j+4]==color):
                return 1
    return 0                                                #定义判定胜负函数

def is_kongde(x,y):                                                  #判空函数
    if(qipan[x][y]==2):
        return 1
    else:
        return 0

def AI(colo):
    global qipan
    global index
    global canvas
    color=['red','green']
    kuan=16
    initial_value=2
#1--己方四连A--黑黑黑黑空
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == colo and qipan[i][j + 1] == colo and qipan[i][j + 2] == colo and qipan[i][j + 3] == colo and qipan[i][j + 4] == initial_value):
                j=j+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 1
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == colo and qipan[i + 1][j] == colo and qipan[i + 2][j] == colo and qipan[i + 3][j] == colo and qipan[i + 4][j] == initial_value):
                i=i+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 1
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == colo and qipan[i + 1][j - 1] == colo and qipan[i + 2][j - 2] == colo and qipan[i + 3][j - 3] == colo and qipan[i + 4][j - 4] == initial_value):
                i=i+4
                j=j-4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 1
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == colo and qipan[i + 1][j + 1] == colo and qipan[i + 2][j + 2] == colo and qipan[i + 3][j + 3] == colo and qipan[i + 4][j + 4] == initial_value):
                i=i+4
                j=j+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 1


#2--己方四连B--空黑黑黑黑
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i][j + 1] == colo and qipan[i][j + 2] == colo and qipan[i][j + 3] == colo and qipan[i][j + 4] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 2
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j] == colo and qipan[i + 2][j] == colo and qipan[i + 3][j] == colo and qipan[i + 4][j] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 2
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j - 1] == colo and qipan[i + 2][j - 2] == colo and qipan[i + 3][j - 3] == colo and qipan[i + 4][j - 4] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 2
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i + 1][j + 1] == colo and qipan[i + 2][j + 2] == colo and qipan[i + 3][j + 3] == colo and qipan[i + 4][j + 4] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 2

#3--对方四连A--空白白白白
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i][j + 1] == another_color(colo) and qipan[i][j + 2] == another_color(colo) and qipan[i][j + 3] == another_color(colo) and qipan[i][j + 4] == another_color(colo)):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 3
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j] == another_color(colo) and qipan[i + 2][j] == another_color(colo) and qipan[i + 3][j] == another_color(colo) and qipan[i + 4][j] == another_color(colo)):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 3
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j - 1] == another_color(colo) and qipan[i + 2][j - 2] == another_color(colo) and qipan[i + 3][j - 3] == another_color(colo) and qipan[i + 4][j - 4] == another_color(colo)):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 3
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i + 1][j + 1] == another_color(colo) and qipan[i + 2][j + 2] == another_color(colo) and qipan[i + 3][j + 3] == another_color(colo) and qipan[i + 4][j + 4] == another_color(colo)):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 3


#4--对方四连B--白白白白空
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == another_color(colo) and qipan[i][j + 1] == another_color(colo) and qipan[i][j + 2] == another_color(colo) and qipan[i][j + 3] == another_color(colo) and qipan[i][j + 4] == initial_value):
                j=j+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 4
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == another_color(colo) and qipan[i + 1][j] == another_color(colo) and qipan[i + 2][j] == another_color(colo) and qipan[i + 3][j] == another_color(colo) and qipan[i + 4][j] == initial_value):
                i=i+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 4
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == another_color(colo) and qipan[i + 1][j - 1] == another_color(colo) and qipan[i + 2][j - 2] == another_color(colo) and qipan[i + 3][j - 3] == another_color(colo) and qipan[i + 4][j - 4] == initial_value):
                i=i+4
                j=j-4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 4
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == another_color(colo) and qipan[i + 1][j + 1] == another_color(colo) and qipan[i + 2][j + 2] == another_color(colo) and qipan[i + 3][j + 3] == another_color(colo) and qipan[i + 4][j + 4] == initial_value):
                i=i+4
                j=j+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 3

#5--对方三连A--空白白白空
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i][j + 1] == another_color(colo) and qipan[i][j + 2] == another_color(colo) and qipan[i][j + 3] == another_color(colo) and qipan[i][j + 4] == initial_value):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j] == another_color(colo) and qipan[i + 2][j] == another_color(colo) and qipan[i + 3][j] == another_color(colo) and qipan[i + 4][j] == initial_value):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j - 1] == another_color(colo) and qipan[i + 2][j - 2] == another_color(colo) and qipan[i + 3][j - 3] == another_color(colo) and qipan[i + 4][j - 4] == initial_value):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i + 1][j + 1] == another_color(colo) and qipan[i + 2][j + 2] == another_color(colo) and qipan[i + 3][j + 3] == another_color(colo) and qipan[i + 4][j + 4] == initial_value):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5

#6--对方三连B--空白白白黑
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i][j + 1] == another_color(colo) and qipan[i][j + 2] == another_color(colo) and qipan[i][j + 3] == another_color(colo) and qipan[i][j + 4] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 6
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j] == another_color(colo) and qipan[i + 2][j] == another_color(colo) and qipan[i + 3][j] == another_color(colo) and qipan[i + 4][j] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 6
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == initial_value and qipan[i + 1][j - 1] == another_color(colo) and qipan[i + 2][j - 2] == another_color(colo) and qipan[i + 3][j - 3] == another_color(colo) and qipan[i + 4][j - 4] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 6
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == initial_value and qipan[i + 1][j + 1] == another_color(colo) and qipan[i + 2][j + 2] == another_color(colo) and qipan[i + 3][j + 3] == another_color(colo) and qipan[i + 4][j + 4] == colo):
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 6

#7--对方三连C--黑白白白空
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] ==colo and qipan[i][j + 1] == another_color(colo) and qipan[i][j + 2] == another_color(colo) and qipan[i][j + 3] == another_color(colo) and qipan[i][j + 4] == initial_value):
                j=j+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == colo and qipan[i + 1][j] == another_color(colo) and qipan[i + 2][j] == another_color(colo) and qipan[i + 3][j] == another_color(colo) and qipan[i + 4][j] == initial_value):
                i=i+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == colo and qipan[i + 1][j - 1] == another_color(colo) and qipan[i + 2][j - 2] == another_color(colo) and qipan[i + 3][j - 3] == another_color(colo) and qipan[i + 4][j - 4] == initial_value):
                i=i+4
                j=j-4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] ==colo  and qipan[i + 1][j + 1] == another_color(colo) and qipan[i + 2][j + 2] == another_color(colo) and qipan[i + 3][j + 3] == another_color(colo) and qipan[i + 4][j + 4] == initial_value):
                i=i+4
                j=j+4
                qipan[i][j] = colo
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
                return 5

#8--己方三连
#横排
    for i in range(16):
        for j in range(12):
            if (qipan[i][j] == colo and qipan[i][j + 1] == colo and qipan[i][j + 2] == colo and qipan[i][j + 3] == colo and qipan[i][j + 4] == colo):
                return 1
#竖排
    for i in range(12):
        for j in range(16):
            if (qipan[i][j] == colo and qipan[i + 1][j] == colo and qipan[i + 2][j] == colo and qipan[i + 3][j] == colo and qipan[i + 4][j] == colo):
                return 1
#副对角线
    for i in range(12):
        for j in range(4,16):
            if (qipan[i][j] == colo and qipan[i + 1][j - 1] == colo and qipan[i + 2][j - 2] == colo and qipan[i + 3][j - 3] == colo and qipan[i + 4][j - 4] == colo):
                return 1
#主对角线
    for i in range(12):
        for j in range(12):
            if (qipan[i][j] == colo and qipan[i + 1][j + 1] == colo and qipan[i + 2][j + 2] == colo and qipan[i + 3][j + 3] == colo and qipan[i + 4][j + 4] == colo):
                return 1
    while(True):
        i=int(randint(0,15))
        j=int(randint(0,15))
        if(is_kongde(i,j)==1):
            qipan[i][j]=colo
            canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='%s'%color[colo],tags=('chess'))
            break
    index+=1
    if (is_win(0)==1):                                 #判断是否获胜，若获胜：弹窗退出游戏
        print('%s棋赢了'%col[0])
        var_top.set('%s棋赢了'%col[0])
        showinfo('%s棋赢了'%col[0], '%s棋赢了，游戏结束'%col[0])
        os._exit(0)
    return 0

def loser():                                                         #定义认输操作
    col=['绿','红']
    global on_hit
    global index
    global var_top

    if (AI_mode==True):
        var_top.set('人方认输，游戏结束')
        showinfo('人方认输，游戏结束','人方认输，游戏结束')
        os._exit(0)

    index%2==1
    var_top.set('%s方认输，游戏结束'%col[index%2])
    showinfo('%s方认输，游戏结束'%col[index%2],'%s方认输，游戏结束'%col[index%2])

    os._exit(0)

def play_AI(event):                                                  #定义落子操作
        global back_x,back_y,last
        global index
        global hui
        color=['red','green']
        col=['红','绿']
        x=event.x                                                    #获取鼠标点击坐标
        y=event.y
        y=int((y+15)/30)*30                                          #利用鼠标点击坐标计算出落子坐标
        x=int((x+15)/30)*30
        if(is_kongde(int((x+15)/30),int((y+15)/30))==1):
            index=index+1
            last=color[1]                                      #将棋子颜色存入全局变量“last”，用于悔棋操作
            fequency=[440,494,554,587,659,740,831,880]               #定义音阶频率
            winsound.Beep(fequency[index%8],300)                     #发出落子音效
            canvas.create_oval(x-10,y-10,x+10,y+10,fill='%s'%color[1],tags=('chess'))
            var_top.set('轮到绿棋下子')
            global qipan                                             #声明全局数组变量“qipan”
            qipan[int((x+15)/30)][int((y+15)/30)]=1           #将落子情况存入数组“qipan”
            back_x=int((x+15)/30)                                         #将棋子坐标存入全局变量“a”,“b”，用于悔棋操作
            back_y=int((y+15)/30)
            if (is_win(1)==1):                                 #判断是否获胜，若获胜：弹窗退出游戏
                print('%s棋赢了'%col[1])
                var_top.set('%s棋赢了'%col[1])
                showinfo('%s棋赢了'%col[1], '%s棋赢了，游戏结束'%col[1])
                os._exit(0)
            if(hui==0):
                AI(0)
                if (is_win(0)==1):                                 #判断是否获胜，若获胜：弹窗退出游戏
                    print('%s棋赢了'%col[0])
                    var_top.set('%s棋赢了'%col[0])
                    showinfo('%s棋赢了'%col[0], '%s棋赢了，游戏结束'%col[0])
                    os._exit(0)
            else:
                hui=0
        return 0

def play(event):                                                     #定义落子操作
        global back_x,back_y,last
        color=['red','green']
        col=['红','绿']
        global index
        x=event.x                                                    #获取鼠标点击坐标
        y=event.y
        y=int((y+15)/30)*30                                          #利用鼠标点击坐标计算出落子坐标
        x=int((x+15)/30)*30
        if(is_kongde(int((x+15)/30),int((y+15)/30))==1):
            index=index+1
            last=color[index%2]                                      #将棋子颜色存入全局变量“last”，用于悔棋操作
            fequency=[440,494,554,587,659,740,831,880]               #定义音阶频率
            winsound.Beep(fequency[index%8],300)                     #发出落子音效
            canvas.create_oval(x-10,y-10,x+10,y+10,fill='%s'%color[index%2],tags=('chess'))
            var_top.set('轮到%s棋下子'%col[(1+index)%2])
            global qipan                                             #声明全局数组变量“qipan”
            qipan[int((x+15)/30)][int((y+15)/30)]=index%2            #将落子情况存入数组“qipan”
            back_x=int((x+15)/30)                                         #将棋子坐标存入全局变量“a”,“b”，用于悔棋操作
            back_y=int((y+15)/30)
            if (is_win(index%2)==1):                                 #判断是否获胜，若获胜：弹窗退出游戏
                print('%s棋赢了'%col[index%2])
                var_top.set('%s棋赢了'%col[index%2])
                showinfo('%s棋赢了'%col[index%2], '%s棋赢了，游戏结束'%col[index%2])
                os._exit(0)
        return 0

def goback():
    global canvas
    global index
    global back_x,back_y
    global hui
    canvas.delete('chess')                                           #删除界面中所有棋子图案
    var = StringVar()                                                #设置文字变量储存器
    label= Label(root,textvariable=var ,bg='red', width=15, height=2)#使用 textvariable 替换 text, 因为这个可以变化
    var.set('%s方悔棋'%last)
    label.pack()

    qipan[back_x][back_y]=2                                                    #在全局数组变量“qipan”中，将悔棋位置标记为空白
    for i in range(16):                                              #根据全局数组变量“qipan”中的数据，重新绘制所有棋子
        for j in range(16):
            if(qipan[i][j]==0):
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='red',tags=('chess'))
            elif(qipan[i][j]==1):
                canvas.create_oval((i*30)-10,(j*30)-10,(i*30)+10,(j*30)+10,fill='green',tags=('chess'))
    index=index+1                                                    #更新落子计数器
    if (AI_mode==True):
        index+=1
    hui=1
    return 0

#函数结束


#创建窗口
root=Tk()
root.title("五子棋游戏")
root.geometry('600x630')                                             #设置窗口大小
root.iconbitmap('favicon.ico')

#画布，棋盘描绘
canvas=Canvas(root,height=450,width=450)                             #初始化画布变量“canvas”
image_file=PhotoImage(file='3.png')                                  #读取图片
image=canvas.create_image(225,225,anchor='center',image=image_file)  #将图片导入画布
i=30
while i<450:                                                         #绘制棋盘网格
    canvas.create_line(i,0,i,450)
    canvas.create_line(0,i,450,i)
    i=i+30
var_top= StringVar()                                                 #设置文字变量储存器

label= Label(root,textvariable=var_top,bg='red',width=15,height=2)       #使用 textvariable 替换 text, 因为这个可以变化
label.pack()
var_top.set('轮到%s棋下子'%col[(1+index)%2])


AI_mode=askyesno('游戏模式', '是否进入人机练习模式？')                 #返回并保存弹窗返回值'True'or'False'
if (AI_mode==False):
    canvas.bind("<Button-1>",play)                                   #绑定鼠标左键，并调用落子操作
elif(AI_mode==True):
    canvas.bind("<Button-1>",play_AI)
canvas.pack()


button_exit=Button(root,text='认输，结束游戏',width=15,height=2, command=loser)
button_exit.pack()
button_undo=Button(root,text='悔棋',width=15,height=2,command=goback)#定义“悔棋”按钮
button_undo.pack()


root.mainloop()                                                      #进入到事件（消息）循环
