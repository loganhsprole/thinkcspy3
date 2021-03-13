import turtle
wn = turtle.Screen()

star = turtle.Turtle()

star.hideturtle()

for x in range(5):
    star.right(720/5)
    star.forward(100)

star.showturtle()

wn.mainloop()
