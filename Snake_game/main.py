from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

snake_parts = [1,2,3]
start_position = [0,-20,-40]
for part in range(0,3):
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    snake_part.goto(start_position[part],0)


    snake_parts.append(part)





screen.exitonclick()

