import turtle as t
import random as r


def change_color():
    red = r.randint(0,255)
    blue = r.randint(0,255)
    green = r.randint(0,255)
    rgb = (red, green, blue)
    return rgb


screen = t.Screen()
screen.bgcolor("black")
screen.colormode(255)

turtle = t.Turtle()
turtle.speed("fastest")
while True:
    turtle.pencolor(change_color())
    turtle.circle(100)
    turtle.position()
    turtle.setheading(turtle.heading()+1)

screen.exitonclick()

