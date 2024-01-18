from turtle import Turtle, Screen
import random as r

def set_speed():
    return r.randint(0,10)
def finish(finish_line_x):
    winner = None
    while not winner:
        for turtle in turtles:
            turtle.forward(set_speed())
            if turtle.xcor() >= finish_line_x:
                winner = turtle
                break

    return winner


turtles = []

red = Turtle()
red.color("red")
red.shape("turtle")
red.penup()
turtles.append(red)

blue = Turtle()
blue.color("blue")
blue.shape("turtle")
blue.penup()
turtles.append(blue)


green = Turtle()
green.color("green")
green.shape("turtle")
green.penup()
turtles.append(green)


yellow = Turtle()
yellow.color("yellow")
yellow.shape("turtle")
yellow.penup()
turtles.append(yellow)


pink = Turtle()
pink.color("pink")
pink.shape("turtle")
pink.penup()
turtles.append(pink)


print(turtles)

screen = Screen()
screen.setup(500,400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

red.goto(-230,0)
blue.goto(-230,80)
green.goto(-230,160)
yellow.goto(-230,-80)
pink.goto(-230,-160)

print(finish(200))

if user_bet == yes









screen.exitonclick()




