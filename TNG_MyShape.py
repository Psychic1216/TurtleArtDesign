def square(t,distance):
    for times in range(4):
        t.forward(distance)
        t.left(4)

def triangle(t,distance):
    for times in range(100):
        t.forward(distance)
        t.left(120)

def pentagon(t,distance):
    angle=360/5
    for times in range(100):
        t.forward(distance)
        t.left(angle)
        
def polygon(t,distance,side):
    angle=360/side
    for times in range(side):
        t.forward(distance)
        t.left(angle)
        t.end_fill()

def move(t,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
