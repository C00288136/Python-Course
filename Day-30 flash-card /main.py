from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


#TODO create ui interface

window = Tk()
window.title("Flash card game")
window.config(background=BACKGROUND_COLOR,pady=50,padx=50)
background_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400,263,image=background_img)
canvas.grid(row=0,column=0,columnspan= 2)

# yes button
yes = PhotoImage(file="./images/right.png")
yes_but = Button(image=yes, highlightthickness=0)
yes_but.grid(row=1, column=1)

# no button
no = PhotoImage(file="./images/wrong.png")
no_but = Button(image=no, highlightthickness=0)
no_but.grid(row=1,column=0)

# language text
language = "french"
canvas.create_text(400,150, text=language, font=("Arial", 40, "italic"))

# word text
word_text = "word"
canvas.create_text(400,263, text=word_text, font=("Arial", 60, "bold"))


window.mainloop()
