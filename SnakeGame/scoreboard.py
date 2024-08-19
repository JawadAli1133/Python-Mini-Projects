from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.refresh_score()
        self.hideturtle()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))

    def increment_score(self):
        self.score += 1
        self.refresh_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_score()

    def get_highscore(self):
        with open("score.txt") as file:
            high_score = int(file.read())
            return high_score

    def save_highscore(self):
        with open("score.txt",'w') as file:
            file.write(str(self.high_score))

