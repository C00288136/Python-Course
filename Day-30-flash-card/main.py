import random
from tkinter import *
import pandas as pd

# basic project for practising words in a specified language
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# TODO make the dictionary for words
# change the file paths to a language of your choosing
try:

<<<<<<< HEAD
df = pd.read_csv("data/french_words.csv")
data = df.to_dict(orient="records")
=======
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")
>>>>>>> 7b1d49751bf51d0f95fcc1ddff48afa877571ac6


# TODO create function for yes button
def yes_confirm():
    print("yes")
    data.remove(current_card)
    learn = pd.DataFrame(data)
    learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# TODO create function for no button
def no_confirm():
    print("no")


# TODO create function for choosing random word:
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    print(current_card["French"])
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    # change the French word to wanted language
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=background_img)
    # timer used to delay the change of the word to english can be modified
    flip_timer = window.after(3000, change_to_english)


def change_to_english():
    print("ran")
    english = current_card["English"]
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(card_text, text=english, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")


# TODO create ui interface

window = Tk()
window.title("Flash card game")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)
background_img = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=background_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, change_to_english)

# yes button
yes = PhotoImage(file="./images/right.png")
yes_but = Button(image=yes, highlightthickness=0, command=yes_confirm)
yes_but.grid(row=1, column=1)

# no button
no = PhotoImage(file="./images/wrong.png")
no_but = Button(image=no, highlightthickness=0, command=no_confirm)
no_but.grid(row=1, column=0)

# language text
language = "french"
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

# word text
word_text = "word"
card_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

next_card()
window.mainloop()
