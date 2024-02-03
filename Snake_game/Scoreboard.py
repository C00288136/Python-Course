from turtle import Turtle

with open("data.txt") as file:
    file.read()
with open("data.txt") as file:
    saved = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(saved)

        # self.score.penup()
        self.hideturtle()
        self.goto(-50, 280)
        self.color('white')
        self.update_scoreboard()

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} High Score : {self.highscore}", align="left",
                   font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with (open("data.txt", mode="w") as update):
            update = update.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
