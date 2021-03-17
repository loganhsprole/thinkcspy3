import turtle


def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    t.speed(40)
    return t


def make_star(t):
    for i in range(5):
        t.left(360 / 5)
        t.forward(100)
        t.left(144)


wn = make_window("lightgreen", "star")
claire = make_turtle("hotpink", 2)

for i in range(5):
    make_star(claire)
    claire.penup()
    claire.forward(350)
    claire.right(144)
    claire.pendown()

wn.mainloop()
