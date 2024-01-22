from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()

game_on = True
while game_on:
    screen.update()
    # screen update make it so the graphics of the snake update, and they piece don't move individually 1 by 1
    time.sleep(0.1)
    snake.move()
    # because the 3 pieces of the snake are not connected we need this method to make sure that the snake looks as if
    # it is connected the last piece is moved into the position of the second last which keeps the flow
screen.exitonclick()
