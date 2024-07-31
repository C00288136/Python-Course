import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 32)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)



tim = t.Turtle()
t.colormode(255)
color_list =[(254, 254, 253), (219, 254, 237), (84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42), (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220), (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]
tim.hideturtle()
tim.pu()
forward = 50

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    tim.home()
    tim.lt(90)
    tim.forward(forward)
    forward += 50
    print(forward)
    tim.rt(90)





screen = t.Screen()
screen.exitonclick()




