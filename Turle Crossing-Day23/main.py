import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkey(player.move,'Up')

    car_manager.create_cars()
    car_manager.move_car()

#     detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

#     detec finish line
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.levelup()


screen.exitonclick()