import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# TODO make the dictionary for words

df = pd.read_csv("data/french_words.csv")
data = df.to_dict(orient="records")


# TODO create function for yes button
def yes_confirm():
    print("yes")
    pass


# TODO create function for no button
def no_confirm():
    print("no")
    pass


# TODO create function for choosing random word:
def next_card():
    global current_card
    current_card = random.choice(data)
    print(current_card["French"])
    canvas.itemconfig(card_text, text=current_card["French"])
    canvas.itemconfig(card_title, text="French")


def change_to_english():
    english = current_card["English"]


# TODO create ui interface

window = Tk()
window.title("Flash card game")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)
background_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=background_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# yes button
yes = PhotoImage(file="./images/right.png")
yes_but = Button(image=yes, highlightthickness=0, command=next_card)
yes_but.grid(row=1, column=1)

# no button
no = PhotoImage(file="./images/wrong.png")
no_but = Button(image=no, highlightthickness=0, command=next_card)
no_but.grid(row=1, column=0)

# language text
language = "french"
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

# word text
word_text = "word"
card_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

next_card()
window.mainloop()

window.after(3000, )
