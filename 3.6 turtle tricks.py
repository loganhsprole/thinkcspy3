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
claire.shape("turtle")
claire.speed(0)

colors = ["yellow", "red", "purple", "blue"]
for c in colors:
    claire.color(c)
    claire.forward(50)
    claire.left(90)

claire.penup()
claire.forward(100)
claire.pendown()

frog = turtle.Turtle()
frog.shape("turtle")
frog.color("blue")

frog.penup()
frog_size = 20
for y in range(30):
    frog.stamp()
    frog_size = frog_size + 3
    frog.forward(frog_size)
    frog.right(24)

frog.color("red")

wn.mainloop()
