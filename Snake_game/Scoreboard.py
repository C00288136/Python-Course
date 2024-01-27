from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        score = 0

        # self.score.penup()
        self.hideturtle()
        self.goto(-50, 280)
        self.color('white')
        self.previous_score = score
        self.update_scoreboard()


    def point(self):
        self.previous_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.previous_score}", align="left", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",20,"bold"))
