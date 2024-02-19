from tkinter  import *

window = Tk()
window.title("Miles to km Converter")

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label= Label(text="Miles")
miles_label.grid(column=2,row=0)

equal = Label(text="is equal to")


km_result = Label(text=0)

kms = Label(text="km")

convert = Button(text="Convert")