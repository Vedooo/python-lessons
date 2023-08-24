from tkinter import *
import time
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    
    ui.after(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_sign.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 1:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps %2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer =ui.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        tick_sign.config(text=marks)
            

# ---------------------------- UI SETUP ------------------------------- #

ui = Tk()
ui.title("Pomodoro Timer")
ui.config(padx=100,pady=50, bg=YELLOW)

photo = PhotoImage(file="tomato.png")

canvas = Canvas(width=250, height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(120,112,image=photo)
timer_text = canvas.create_text(122, 129, text="00:00", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(column=2,row=2)

# Labels

timer_label = Label(text="Timer", font=(FONT_NAME,45),fg=GREEN,bg=YELLOW)
timer_label.grid(column=2,row=0)
timer_label.config(padx=5,pady=20)

tick_sign = Label(font=(FONT_NAME,35),fg=GREEN,bg=YELLOW)
tick_sign.grid(column=2,row=4)
tick_sign.config(padx=10,pady=10)

# Buttons

## Start Button
start_button = Button(text="Start", font=(FONT_NAME,20,"bold"),fg="black",bg=YELLOW, command=start_timer)
start_button.config(padx=10,pady=10)
start_button.grid(column=1,row=4)

## End Button
reset_button = Button(text="Reset", font=(FONT_NAME,20,"bold"),fg="black",bg=YELLOW,command=reset_timer)
reset_button.config(padx=5,pady=5)
reset_button.grid(column=3,row=4)

count_down(5)
ui.mainloop()