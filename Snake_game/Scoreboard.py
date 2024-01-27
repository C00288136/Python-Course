from turtle import Turtle


class Scoreboard:
    def __init__(self):
        score = 0
        self.score = Turtle()
        # self.score.penup()
        self.score.hideturtle()
        self.score.goto(-50, 280)
        self.score.color('white')
        self.previous_score = score
        self.update_scoreboard()


    def point(self):
        self.previous_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score.clear()
        self.score.write(f"Scoreboard: {self.previous_score}", align="left", font=("Arial", 12, "normal"))
