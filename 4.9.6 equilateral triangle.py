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


def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)


wn = make_window("lightgreen", "triangle")
claire = make_turtle("hotpink", 3)
draw_equitriangle(claire, 50)

wn.mainloop()