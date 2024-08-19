import turtle as t

screen = t.Screen()
screen.bgcolor("white")
screen.colormode(255)

turtle = t.Turtle()
turtle.color("black")


def move_right():
    turtle.setheading(turtle.heading()-10)
    # turtle.forward(20)


def move_left():
    turtle.setheading(turtle.heading()+10)
    # turtle.forward(20)


def move_up():
    turtle.forward(20)


def move_down():
    turtle.setheading(turtle.heading()+180)
    # turtle.forward(20)


def clear():
    turtle.clear()


turtle.speed("fastest")

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(clear, "c")

screen.mainloop()

screen.exitonclick()