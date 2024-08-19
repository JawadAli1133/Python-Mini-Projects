from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.x_shift = 10
        self.y_shift = 10
        self.move_speed = 0.1

    def refresh(self):
        self.goto(self.xcor()+self.x_shift, self.ycor()+self.y_shift)

    def bounce_y(self):
        self.y_shift *= -1

    def bounce_x(self):
        self.x_shift *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
