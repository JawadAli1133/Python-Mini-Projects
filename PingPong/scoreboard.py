from turtle import Turtle


class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(position)
        self.refresh()

    def refresh(self):
        self.write(f"{self.score}",move=False,align="center",font=("Courier", 80, "normal"))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.refresh()
