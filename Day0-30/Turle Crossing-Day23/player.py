from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape("turtle")
        self.lt(90)
        self.go_to_start()
        self.penup()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.teleport(STARTING_POSITION[0],STARTING_POSITION[1])

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
