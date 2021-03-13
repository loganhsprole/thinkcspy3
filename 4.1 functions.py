import turtle

__import__("turtle").__traceable__ = False


def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

claire = turtle.Turtle()
claire.pensize(3)
claire.shape("turtle")

size = 20
for i in range(15):
    draw_multicolor_square(claire, size)
    size = size + 10
    claire.forward(10)
    claire.right(18)

wn.mainloop()
