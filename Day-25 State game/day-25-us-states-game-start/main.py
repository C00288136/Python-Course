import pandas
import turtle

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game ")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

correct_guess = 0

while correct_guess < len(data["state"]):
    answer_state = screen.textinput(title=f"Guess the state {correct_guess}/{len(data["state"])}",prompt="What is another states name")

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        correct_guess +=1
        screen.update()



# If one of states make a turtle and write its name onto the map
turtle.Turtle()






