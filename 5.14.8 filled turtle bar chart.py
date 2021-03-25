import turtle


def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(sz):
    t = turtle.Turtle()
    t.pensize(sz)
    return t


def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


xs = [48, 117, 200, 240, 160, 260, 220]
wn = make_window("lightgreen", "bar chart")
artist = make_turtle(3)

for v in xs:
    if v >= 200:
        artist.color("blue", "red")
    elif v >= 100 and v < 200:
        artist.color("blue", "yellow")
    elif v < 100:
        artist.color("blue", "green")
    draw_bar(artist, v)

wn.mainloop()