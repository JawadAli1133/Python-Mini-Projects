import colorgram as c
import turtle as t
import random as r

colors = c.extract("download.jpg", 100)

rgb_colors = []
for color in colors:
    r_val = color.rgb.r
    b_val = color.rgb.b
    g_val = color.rgb.g
    rgb_colors.append((r_val, g_val, b_val))


screen = t.Screen()
screen.bgcolor("white")
screen.colormode(255)

turtle = t.Turtle()

screen_width = screen.window_width()
screen_height = screen.window_height()

bottom_left_x = -screen_width // 2
bottom_left_y = -screen_height // 2

turtle.penup()
turtle.goto(bottom_left_x, bottom_left_y)
turtle.pendown()


def draw_dot():
    global turtle
    turtle.dot(30, r.choice(rgb_colors))


for i in range(10):
    for _ in range(10):
        draw_dot()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    turtle.penup()
    turtle.goto(bottom_left_x, bottom_left_y + ((i+1)*50))
    turtle.pendown()


screen.exitonclick()
