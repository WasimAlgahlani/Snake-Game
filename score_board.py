from turtle import Turtle
SCORE_FONT = ("Arial", 12, "bold")
ALIGNMENT = "center"
END_GAME_FONT = ("Arial", 30, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("high score.txt") as score_data:
            self.high_score = int(score_data.read())
        self.track()

    def track(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 230)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high score.txt", mode="w") as new_score:
                new_score.write(str(self.high_score))
        self.score = -1
        self.track()




