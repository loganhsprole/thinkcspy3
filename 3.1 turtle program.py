import turtle

bcolor = input("background color: ")
tcolor = input("turtle color: ")
tsize = int(input("turtle size: "))
wn = turtle.Screen()

wn.bgcolor(bcolor)
wn.title("Hello, Claire!")

claire = turtle.Turtle()
claire.color(tcolor)
claire.pensize(tsize)

claire.forward(50)
claire.left(120)
claire.forward(50)

wn.mainloop()
