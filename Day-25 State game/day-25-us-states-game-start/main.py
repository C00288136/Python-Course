import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game ")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []
while len(guessed_states) < 50:
    # use the title marker to capitalise every first letter
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_states)}/{len(data["state"])}",
                                    prompt="What is another states name").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        break
        # create a csv of the states you didn't guess
        new_csv = pandas.DataFrame(missing_states)
        new_csv.to_csv("States_to_learn.csv")
        # all the data for the row described in saved in state_data

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        screen.update()




