from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
# image looks for x and y position from the top on the canvas
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# TODO all the labels for the file
Website_name = Label(text="Website:")
Website_name.grid(column=0, row=1)

email_username = Label(text="Email/Username")
email_username.grid(column=0, row=2)

password_text = Label(text="Password")
password_text.grid(column=0, row=3)

# TODO all the input boxes
Website_in = Entry(width=35)
Website_in.grid(column=1, row=1, columnspan=2)

email_in = Entry(width=35)
email_in.grid(column=1, row=2, columnspan=2)

password_in = Entry(width=21)
password_in.grid(column=1, row=3)

# BUTTON
password_generate = Button(text="Generate Password")
password_generate.grid(column=2, row=3)

submit_button = Button(text="Add", width=36)
submit_button.grid(column=1, row=5)

window.mainloop()
