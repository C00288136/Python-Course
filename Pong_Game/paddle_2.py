from turtle import Turtle
UP = 90
DOWN = 270
class Paddle_2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        self.teleport(350,0)
        self.color('White')
        self.penup()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)