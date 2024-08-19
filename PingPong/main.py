from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time as t

# Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)
screen.colormode(255)

# Adding all the objects
right_paddle = Paddle((370, 100))
left_paddle = Paddle((-370, 100))
ball = Ball()
right_score = Score((-40, 200))
left_score = Score((40, 200))
screen.update()

# Checking the key presses
screen.listen()
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")

game_run = True
while game_run:
    ball.refresh()
    screen.update()
    t.sleep(ball.move_speed)

    # Detect collision of ball with wall (vertical)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) <= 50
                                                                     and ball.xcor() < -340):
        ball.bounce_x()

    # Detect collision of ball with (horizontal)
    if ball.distance(right_paddle) > 50 and ball.xcor() > 380:
        ball.reset_position()
        left_score.increment_score()
    if ball.distance(left_paddle) > 50 and ball.xcor() < -380:
        ball.reset_position()
        right_score.increment_score()

screen.exitonclick()
