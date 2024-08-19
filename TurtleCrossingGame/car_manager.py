import random as r
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        car = Turtle()
        car.color(r.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(300, r.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())

    def remove_cars(self):
        for car in self.cars:
            if car.xcor() <= -300:
                car.hideturtle()
                self.cars.remove(car)
    def increment_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
