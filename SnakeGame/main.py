import turtle as t
import snake as s
import time
from food import Food
from scoreboard import Score

# Setting up the screen
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)


snake = s.Snake()
screen.update()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_run = True
while game_run:
    screen.update()
    snake.move(screen)
    time.sleep(0.1)

    if snake.head.distance(food) < 20:
        food.refresh()
        score.increment_score()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()
        score.save_highscore()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
            score.save_highscore()
screen.exitonclick()
