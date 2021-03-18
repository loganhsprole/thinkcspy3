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


def make_spiral(t, trn):
    for i in range(1, 199, 2):
        t.right(trn)
        t.forward(i)
    t.right(trn)


wn = make_window("lightgreen", "spirals")
claire = make_turtle("blue", 1)
logan = make_turtle("blue", 1)

claire.penup()
claire.backward(150)
claire.pendown()
make_spiral(claire, 90)

logan.penup()
logan.forward(150)
logan.pendown()
make_spiral(logan, 89)

wn.mainloop()
