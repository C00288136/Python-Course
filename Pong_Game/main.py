import time
from turtle import Screen
from paddle import Paddle
from paddle_2 import Paddle_2
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle_2()
ball = Ball()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.listen()
    screen.onkey(player_1.up, "w")
    screen.onkey(player_1.down, "s")
    screen.onkey(player_2.up,"Up")
    screen.onkey(player_2.down,"Down")
    screen.update()
    ball.move()



screen.exitonclick()


