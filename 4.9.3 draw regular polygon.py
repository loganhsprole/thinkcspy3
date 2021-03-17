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


def draw_poly(t, n, sz):
    for j in range(n):
        t.forward(sz)
        t.left(360 / n)


wn = make_window("lightgreen", "polygon")
claire = make_turtle("hotpink", 3)
draw_poly(claire, 8, 50)

wn.mainloop()
