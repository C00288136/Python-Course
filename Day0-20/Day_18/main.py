from turtle import Turtle, Screen

tim = Turtle()


tim.shape("turtle")
tim.color("red")

for _ in range(20):
    tim.fd(5)
    tim.pu()
    tim.fd(5)
    tim.pd()
    











screen = Screen()
screen.exitonclick()