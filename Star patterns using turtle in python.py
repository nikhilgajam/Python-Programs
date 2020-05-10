import turtle

a = turtle.Turtle()

a.getscreen().bgcolor("#994444")
a.pensize(3)

a.penup()
a.goto((100, 100))
a.pendown()

#a.speed(100)

def star(var, size):
    if size <= 10:
        return
    else:
        var.begin_fill()
        for i in range(5):
            var.forward(size)
            star(var, size/3)
            var.left(216)
            print(i)
        var.end_fill()
            
star(a, 360)
turtle.done()