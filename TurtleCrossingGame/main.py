import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.update()

screen.listen()
screen.onkey(fun=turtle.go_forward, key="w")

car_manager = CarManager()
score = Scoreboard()
screen.update()

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1
    if count == 7:
        car_manager.create_car()
        count = 0

    # Detection of turtle with cars
    for car in car_manager.cars:
        if abs(turtle.xcor() - car.xcor()) < 40 and abs(turtle.ycor() - car.ycor()) < 10:
            score.game_over()
            game_is_on = False

    # When turtle reacher the other end
    if turtle.ycor() > 270:
        turtle.reset_position()
        score.increment_level()
        car_manager.increment_speed()

    car_manager.move_cars()
    car_manager.remove_cars()
screen.exitonclick()
