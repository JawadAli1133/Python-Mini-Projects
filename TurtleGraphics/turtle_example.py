import turtle
import random as r

screen = turtle.Screen()
screen.bgcolor("white")
screen.colormode(255)

turtle = turtle.Turtle()

direction = [90, 180, 270, 360]

turtle.shape("classic")
turtle.color("blue")
turtle.pencolor("black")
turtle.penup()
turtle.goto(turtle.xcor(),turtle.ycor()+90)
turtle.pendown()
turtle.pensize(10)

while True:
    turtle.forward(50)
    turtle.setheading(r.choice(direction))
    turtle.pencolor(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))


screen.exitonclick()

