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
    return t


def make_square(t, ln):
    for i in range(4):
        t.forward(ln)
        t.left(90)


wn = make_window("lightgreen", "squares")
claire = make_turtle("hotpink", 3)

for j in range(5):
    make_square(claire, 20)
    claire.penup()
    claire.forward(40)
    claire.pendown()

wn.mainloop()
