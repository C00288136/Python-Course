from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_back():
    tim.bk(10)
def move_left():
    tim.lt(20)
def move_right():
    tim.rt(20)
def clear():
    tim.clear()
    tim.penup()
    tim.home()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)










screen.exitonclick()


