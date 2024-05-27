from tkinter import *

window = Tk()
window.title("Miles to km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

km_result = Label(text=0)
km_result.grid(column=1, row=1)

kms = Label(text="km")
kms.grid(column=2, row=1)


def buttonclick():
    miles = miles_input.get()
    km = (float(miles) * 1.609)
    km_result.config(text=km)


convert = Button(text="Convert", command=buttonclick)
convert.grid(column=1, row=2)

window.mainloop()
