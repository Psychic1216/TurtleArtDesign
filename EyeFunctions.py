from random import randint
from TNG_MyShape import *

def middle(t,distance,side):
    for times in range(side):
        t.color(255,255,0)
        square(t,distance)
        t.left(50)

def sclera(t,side):
    for x in range(side):
        t.begin_fill()
        square(t,600)
        t.color(180-x,180-x,180-x)
        move(t,0,0)
        polygon(t,100,1)
        t.left(6)
        t.end_fill()

def cornea(t,distance,side):
    angle=360/side
    for times in range(side):
        t.begin_fill()
        t.color(0,0,0)
        move(t,0,0)
        t.circle(distance)
        t.left(angle)
        t.end_fill()
        
def pupil(t,distance,side):
    angle=360/side
    for times in range(side):
        t.begin_fill()
        t.color(80,80,80)
        move(t,0,0)
        t.circle(distance)
        t.left(angle)
        t.end_fill()

