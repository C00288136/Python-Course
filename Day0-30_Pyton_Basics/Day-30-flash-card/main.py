import random
from tkinter import *
import pandas as pd

# Basic project for practising words in a specified language
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Load words from CSV files
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

# Function for yes button
def yes_confirm():
    global to_learn
    to_learn.remove(current_card)
    data_to_save = pd.DataFrame(to_learn)
    data_to_save.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Function for no button
def no_confirm():
    next_card()

# Function for choosing random word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=background_img)
    flip_timer = window.after(3000, change_to_english)

# Function to change the card to show English translation
def change_to_english():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=new_image)

# Create UI interface
window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Load images
background_img = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=background_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Yes button
yes_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=yes_confirm)
yes_button.grid(row=1, column=1)

# No button
no_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=no_confirm)
no_button.grid(row=1, column=0)

flip_timer = window.after(3000, change_to_english)
next_card()

window.mainloop()
