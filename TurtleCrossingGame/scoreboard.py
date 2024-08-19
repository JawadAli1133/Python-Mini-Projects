from turtle import  Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self. color("black")
        self.penup()
        self.level = 0
        self.goto(-240,270)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def increment_level(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",align="left",font=FONT)


