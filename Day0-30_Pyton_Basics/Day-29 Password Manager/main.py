from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_in.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = Website_in.get()
    email = email_in.get()
    password = password_in.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Error", message="Please dont leave any fields empty!!")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # save updated data
                json.dump(new_data, file, indent=4)


        else:
            # update old data
            data.update(new_data)

            with open("data.json", "w") as file:
                # save updated data
                json.dump(data, file, indent=4)
        finally:
            # print(data)
            Website_in.delete(0, END)
            password_in.delete(0, END)
            email_in.delete(0, END)
            email_in.insert(0, "myemail@gmail.com")


# ---------------------------- SEARCH METHOD ------------------------------- #
def find_password():
    try:
        website_name = Website_in.get()
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found.")
    else:

        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for this website saved")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
# image looks for x and y position from the top on the canvas
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# TODO all the labels for the file
Website_name = Label(text="Website:")
Website_name.focus()
Website_name.grid(row=1, column=0)
email_username = Label(text="Email/Username")

email_username.grid(row=2, column=0)
password_text = Label(text="Password")
password_text.grid(row=3, column=0)

# TODO all the input boxes
Website_in = Entry(width=35)
Website_in.grid(row=1, column=1, columnspan=1)
email_in = Entry(width=35)
# prepopulates the email entry to speed up process
email_in.insert(0, "myemail@gmail.com")
email_in.grid(row=2, column=1, columnspan=1)
password_in = Entry(width=21)
password_in.grid(column=1, row=3)

# BUTTON
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1,column=2)
password_generate = Button(text="Generate Password", command=generate_password)
password_generate.grid(row=3, column=2)
submit_button = Button(text="Add", width=36, command=save_password)
submit_button.grid(column=1, row=5)

window.mainloop()
