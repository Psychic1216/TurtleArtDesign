from random import randint
from TNG_MyShape import *

def rainbow(t,side):
    for times in range(side):
        square(t,10)
        t.color(0,0,0)
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        move(t,0,0)
        polygon(t,100,3)
        t.left(6)

def ring(t,distance,side):
    angle=360/side
    for times in range(side):
        move(t,0,0)
        t.begin_fill()
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        t.circle(distance)
        t.left(angle)

def background(t,side):
    for times in range(side):
        t.begin_fill()
        square(t,500)
        t.color(0,0,0)
        move(t,0,0)
        polygon(t,100,1)
        t.left(6)
        t.end_fill()

def middle(t,distance,side):
    for times in range(side):
        t.color(255,255,0)
        square(t,distance)
        t.left(50)

 
