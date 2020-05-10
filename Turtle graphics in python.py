import turtle
# import math

a = turtle.Turtle()

a.speed(100)

a.color("orange", "yellow")

a.begin_fill()

for i in range(1000):
    a.forward(400)
    a.left(170)
    
    if abs(a.pos()) < 1:
        break	

a.end_fill()

turtle.done()