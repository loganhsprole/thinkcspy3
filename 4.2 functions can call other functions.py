import turtle


def draw_rectangle(t, w, h):
    """Get turtle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


def draw_square(tx, sz):
    """Get turtle tx to draw a square of width and height sz."""
    draw_rectangle(tx, sz, sz)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

claire = turtle.Turtle()
claire.pensize(3)
claire.shape("turtle")

draw_square(claire, 50)
draw_rectangle(claire, 50, 100)

wn.mainloop()
