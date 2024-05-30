import random
from turtle import Turtle, Screen
from random import choice

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))


toby = Turtle()
color = ["medium blue","magenta","dark orange","firebrick","chartreuse""deep pink","dim gray",]


toby.shape("turtle")
toby.color("blue")

angle = 360
sides = 3
for _ in range(10):
    # toby.fd(100)
    new_angle = angle / sides
    for _ in range(sides):
        toby.rt(new_angle)
        toby.fd(100)
        
    toby.color(random.choice(color))
    sides += 1
    
        
    











screen = Screen()
screen.exitonclick()