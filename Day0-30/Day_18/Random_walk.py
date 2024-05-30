import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
toby = t.Turtle()
t.colormode(255)
choices = [0 , 90 , 180 , 270]
toby.width(15)
toby.speed("fastest")
for _ in range(500):
    toby.fd(30)
    toby.setheading(random.choice(choices))
    toby.fd
    toby.color(random_color())
    
   
    
    




screen = t.Screen()
screen.exitonclick()