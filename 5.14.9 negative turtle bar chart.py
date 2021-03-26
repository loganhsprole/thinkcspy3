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


def draw_bar(t, height, alignment):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if alignment == True:
        t.penup()
        t.backward(11)
        t.write(" " + str(height))
        t.forward(11)
        t.pendown()
    else:
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


xs = [-100, 48, 117, 200, 240, 160, 260, 220]
wn = make_window("lightgreen", "bar chart")
artist = make_turtle(3)

for v in xs:
    if v >= 200:
        artist.color("blue", "red")
        negative = False
    elif v >= 100 and v < 200:
        artist.color("blue", "yellow")
        negative = False
    elif v >= 0 and v < 100:
        artist.color("blue", "green")
        negative = False
    elif v < 0:
        artist.color("blue", "green")
        negative = True

    draw_bar(artist, v, negative)

wn.mainloop()