
from turtle import Turtle, Screen
import random as r

def set_speed():
    return r.randint(0,10)

screen = Screen()
screen.setup(500,400)

colours = ["red","pink","yellow","green","blue","orange"]
y_axis = [-120,-60,0,60,120,180]

race_on = False
continue_game = True

while continue_game:
    all_turtles=[]
    for turtle in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colours[turtle])
        new_turtle.penup()
        new_turtle.goto(-230, y_axis[turtle])
        all_turtles.append(new_turtle)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
    if user_bet:
        race_on = True

    while race_on:
        for turtle in all_turtles:

            if turtle.xcor() > 220:
                winner = turtle.pencolor()
                if user_bet == winner:
                    print("Congrats you bet on the correct turtle !!.\nYou win")

                    race_on = False
                    break
                else:
                    print(f"You lose {winner} won the race")

                    race_on = False
                    break
            turtle.forward(set_speed())
    play_again = screen.textinput(title="",prompt="Play again")
    if play_again.lower() == "no":
        continue_game = False
    else:
        continue_game = True
        race_on = True
        screen.clear()

screen.bye()





