from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_p1 = 0
        self.score_p2 = 0
        self.goto(-100, 200)
        self.write(self.score_p1   , align="center",font=("Courier", 70, "normal"))
        self.goto(100,200)
        self.write(self.score_p2 , align="center",font=("Courier", 70, "normal"))



    def point(self, player):
        if player == 1:
            self.score_p1 += 1
        elif player == 2:
            self.score_p2 += 1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_p1, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.score_p2, align="center", font=("Courier", 70, "normal"))
