from turtle import Turtle

# Snake class
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        self.snake_parts = []
        for position in STARTING_POSITIONS:
            new_part = Turtle('square')
            new_part.color('white')
            new_part.penup()
            new_part.goto(position)
            self.snake_parts.append(new_part)

    def move(self):
        # because the 3 pieces of the snake are not connected we need this method to make sure that the snake looks
        # as if it is connected the last piece is moved into the position of the second last which keeps the flow

        for segment_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[segment_num - 1].xcor()
            new_y = self.snake_parts[segment_num - 1].ycor()
            self.snake_parts[segment_num].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DIS)


    # each of these sets and changes the direction the snake is heading
    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)


    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)
