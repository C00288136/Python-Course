from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.speedup = 1
        self.xmove = 10
        self.ymove = 10


    def move(self):
        new_y = self.ycor() + self.ymove
        new_x = self.xcor() + self.xmove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1
        # the line above makes is so the y cor always gets reversed when the wall is hit

    def bounce_paddle(self):
        # the opposite of the top and bottom wall and send the ball from paddle to paddle
        self.xmove *= -1

        self.speed(self.speedup)
        print(self.speed())


    def reset(self):
        self.goto(0,0)
        self.xmove *= -1
