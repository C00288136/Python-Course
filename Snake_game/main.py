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
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
screen.exitonclick()
