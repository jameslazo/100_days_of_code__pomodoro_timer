from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Rockwell"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="timer", fg=GREEN)
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        final_countdown(long_break_sec)
        timer_label.config(text="break", fg=RED)
    elif reps % 2 != 0:
        final_countdown(work_sec)
        timer_label.config(text="work", fg=GREEN)
    else:
        final_countdown(short_break_sec)
        timer_label.config(text="task", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def final_countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global checkmark
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, final_countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark += "✔"
            checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
timer_label.config(padx=20, pady=10)

start_button = Button(text="start", bg=YELLOW, font=(FONT_NAME, 20, "normal"), fg=GREEN, highlightthickness=0,
                      borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", bg=YELLOW, font=(FONT_NAME, 20, "normal"), fg=GREEN, highlightthickness=0,
                      borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)
checkmark_label.config(padx=20, pady=5)

window.mainloop()
