import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from paddle_2 import Paddle_2

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle()
player_2 = Paddle_2()
ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.listen()
    screen.onkey(player_1.up, "w")
    screen.onkey(player_1.down, "s")
    screen.onkey(player_2.up, "Up")
    screen.onkey(player_2.down, "Down")
    screen.update()
    ball.move()

    #     detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    #         needs to bounce

    # detect collision with paddles
    # 50px distance past certain point
    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() > -340:
        ball.bounce_paddle()
        if ball.speedup < 10:
            ball.speedup += 1

    if ball.xcor() > 380:
        ball.reset()
        score.point(1)

    if ball.xcor() < -380:
        ball.reset()
        score.point(2)

screen.exitonclick()
