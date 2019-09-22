from graph import *
import random
import time

c=canvas()
canvasSize(700, 900)
windowSize(1000, 900)
penColor(0,50,150)
brushColor(0,50,150)
rectangle(0,0,700,300)
penColor(0,50,150)
brushColor(100,100,100)
polygon(((0,100),(50,50),(100,110),(200,55),(400,200),(500,75),(600,100),(700,50),(700,600),(0,600),(0,100)))
penColor(0,150,0)
brushColor(0,150,0)
polygon(((0,500),(300,500),(300,550),(700,550),(700,900),(0,900),(0,500)))
penColor(0,100,0)
brushColor(0,100,0)
circle(570,670,100)

c.create_oval(50,600,250,700,fill='white',outline='white')
c.create_oval(200,520,250,650,fill='white',outline='white')
c.create_oval(200,500,280,540,fill='white',outline='white')
c.create_oval(220,505,250,530,fill='purple',outline='purple')
c.create_oval(235,510,245,525,fill='black',outline='black')
c.create_oval(225,507,240,515,fill='white',outline='white')
c.create_oval(195,475,225,515,fill='white',outline='white')

c.create_oval(55,650,85,730,fill='white',outline='white')
c.create_oval(55,720,85,780,fill='white',outline='white')
c.create_oval(55,775,95,795,fill='white',outline='white')

c.create_oval(95,660,125,740,fill='white',outline='white')
c.create_oval(95,730,125,790,fill='white',outline='white')
c.create_oval(95,785,135,805,fill='white',outline='white')

c.create_oval(190,650,220,730,fill='white',outline='white')
c.create_oval(190,720,220,780,fill='white',outline='white')
c.create_oval(190,775,230,795,fill='white',outline='white')

c.create_oval(225,660,255,740,fill='white',outline='white')
c.create_oval(225,730,255,790,fill='white',outline='white')
c.create_oval(225,785,265,805,fill='white',outline='white')

def cvetok(x,y):

    c.create_oval(x-10, y-25, x+10, y-10, fill='white', outline='white')
    c.create_oval(x-25, y - 10, x-5, y+ 5, fill='white', outline='white')
    c.create_oval(x +5, y - 10, x +25, y + 5, fill='white', outline='white')
    c.create_oval(x - 10, y+5 , x + 10, y +20, fill='white', outline='white')

    c.create_oval(x - 20, y - 20, x , y - 5, fill='white', outline='white')
    c.create_oval(x , y - 20, x+20, y - 5, fill='white', outline='white')
    c.create_oval(x, y , x + 20, y +15, fill='white', outline='white')
    c.create_oval(x - 20, y , x, y +15, fill='white', outline='white')
    c.create_oval(x - 10, y - 10, x + 10, y + 5, fill='yellow', outline='yellow')





def ff():
    penColor(0, 100, 0)
    brushColor(0, 100, 0)
    circle(570, 670, 100)

    cvetok(540+random.randrange(10),620+random.randrange(10))
    cvetok(605+random.randrange(10),620+random.randrange(10))
    cvetok(630+random.randrange(10),670+random.randrange(10))
    cvetok(510+random.randrange(10),670+random.randrange(10))
    cvetok(570+random.randrange(10),670+random.randrange(10))
    cvetok(540+random.randrange(10),720+random.randrange(10))
    cvetok(605+random.randrange(10),720+random.randrange(10))
def ff2():
    c.create_oval(220, 505, 250, 530, fill='purple', outline='purple')
    c.create_oval(235, 510, 245, 525, fill='black', outline='black')
    c.create_oval(225, 507, 240, 515, fill='white', outline='white')
    c.create_oval(195, 475, 225, 515, fill='white', outline='white')
x=0









def ff4():
    global x
    if x<700:
        x+=5
    else:
        x=0

    penColor(0, 50, 150)
    brushColor(0, 50, 150)
    rectangle(0, 0, 700, 50)
    penColor(255, 255, 0)
    brushColor(255, 255, 0)
    a = rectangle(0, 0, 50, 50)

    moveObjectBy(a,x,0)
def ff3():
    c.create_oval(220, 505, 250, 530, fill='white', outline='white')
onTimer(ff, 500)
onTimer(ff4,10)
onTimer(ff2,200)
onTimer(ff3,1000)
run()