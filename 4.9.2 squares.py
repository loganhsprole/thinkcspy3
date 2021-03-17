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
    for j in range(4):
        t.forward(ln)
        t.left(90)


def next_square(t):
    t.penup()
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(180)
    t.pendown()


wn = make_window("lightgreen", "squares")
claire = make_turtle("hotpink", 3)

sideLn = 20
for i in range(5):
    make_square(claire, sideLn)
    next_square(claire)
    sideLn = sideLn + 20

wn.mainloop()
