from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super.__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.hideturtle()
        self.goto(0,400)
        self.color("white")
        self.updateScore()


    def point(self,player):
        if player == 1:
            self.score_p1 += 1
        elif player == 2:
            self.score_p2 +=1
        self.updateScore()
    def updateScore(self):
        self.clear()
        self.write(f"{self.score_p1} {self.score_p1}")

