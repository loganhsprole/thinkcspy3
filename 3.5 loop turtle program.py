import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Logan and Claire")

logan = turtle.Turtle()
logan.color("green")
logan.pensize(8)

for x in range(3):
    logan.forward(80)
    logan.left(120)

logan.right(180)
logan.forward(80)

claire = turtle.Turtle()

colors = ["yellow", "red", "purple", "blue"]
for c in colors:
    claire.color(c)
    claire.forward(50)
    claire.left(90)

wn.mainloop()
