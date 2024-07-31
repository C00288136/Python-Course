from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
window = Tk()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    #     timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label Timer
    Timer_text.config(text="Timer")
    # reset checkmarks
    Check.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        Timer_text.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        Timer_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        Timer_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60

    # these 2 if statements used for formatting the seconds

    if count_seconds < 10:
        count_sec = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS / 2)):
            mark += "✔"
        Check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window.title('Pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)

# timer text
Timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
Timer_text.grid(column=1, row=0)

# Checkmark
Check = Label()
Check.config(bg=YELLOW, fg=GREEN)
Check.grid(column=1, row=3)

# start button
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

# reset button
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

# image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
