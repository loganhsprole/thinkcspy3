import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Logan and Claire")

logan = turtle.Turtle()
logan.color("green")
logan.pensize(8)

claire = turtle.Turtle()

logan.forward(80)
logan.left(120)
logan.forward(80)
logan.left(120)
logan.forward(80)
logan.left(120)

logan.right(180)
logan.forward(80)

claire.forward(50)
claire.left(90)
claire.forward(50)
claire.left(90)
claire.forward(50)
claire.left(90)
claire.forward(50)
claire.left(90)

wn.mainloop()
