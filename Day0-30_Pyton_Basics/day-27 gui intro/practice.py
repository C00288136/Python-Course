# usually use # so everything gets imported
from tkinter import *

# import tkinter

# Tk used for window / frame
window = Tk()
window.title("first gui")
window.minsize(width= 500,height=300)
window.config(padx=20,pady=20)

# Labels
my_label = Label(text="I am a label", font=("Arial",24,"bold"))
# pack adds label to centre of program
# can add top bottom left right for alignment
my_label.grid(column=0,row=0)

my_label["text"] = "yes"
my_label.config(text= "New text")

# button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
# command is a action listener
button = Button(text="click me", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="New button")
button2.grid(column=2,row=3)

# entry
input = Entry(width=10)
input.grid(column=3,row=2)

my_label.mainloop()

