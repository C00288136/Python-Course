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
toby.speed("fastest")
def draw_spirograph(size):
    
    for _ in range(int(360 / size)):
        toby.color(random_color())
        toby.circle(100)
        toby.setheading(toby.heading() + size)
        
    
        
    
draw_spirograph(10.0)



screen = t.Screen()
screen.exitonclick()