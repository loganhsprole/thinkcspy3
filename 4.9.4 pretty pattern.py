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
    t.shape("turtle")
    return t


wn = make_window("lightgreen", "pretty pattern")
claire = make_turtle("blue", 3)


def make_square(t):
    for j in range(20):
        for i in range(4):
            claire.forward(100)
            claire.left(90)
        claire.left(90/5)


make_square(claire)

wn.mainloop()
