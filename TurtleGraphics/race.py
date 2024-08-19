import turtle as t
import random as r

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place a bet.", prompt="Which turtle you think will win the race? ")
game_run = True

def create_turtle(color):
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.speed(10)
    return turtle


green_turtle = create_turtle("green")
red_turtle = create_turtle("red")
purple_turtle = create_turtle("purple")
blue_turtle = create_turtle("blue")
black_turtle = create_turtle("black")
yellow_turtle = create_turtle("yellow")


green_turtle.goto(-230,120)
red_turtle.goto(-230,80)
purple_turtle.goto(-230,40)
blue_turtle.goto(-230,0)
black_turtle.goto(-230,-40)
yellow_turtle.goto(-230,-80)


while game_run:
    green_turtle.forward(r.randint(5,10))
    red_turtle.forward(r.randint(5,10))
    purple_turtle.forward(r.randint(5,10))
    blue_turtle.forward(r.randint(5,10))
    black_turtle.forward(r.randint(5,10))
    yellow_turtle.forward(r.randint(5,10))


screen.exitonclick()


