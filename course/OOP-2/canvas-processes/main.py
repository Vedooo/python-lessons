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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    
    
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        ui.after(1000, count_down, count - 1)

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

tick_sign = Label(text="✓", font=(FONT_NAME,35),fg=GREEN,bg=YELLOW)
tick_sign.grid(column=2,row=4)
tick_sign.config(padx=10,pady=10)

# Buttons

## Start Button
start_button = Button(text="Start", font=(FONT_NAME,20,"bold"),fg="black",bg=YELLOW, command=start_timer)
start_button.config(padx=10,pady=10)
start_button.grid(column=1,row=4)

## End Button
reset_button = Button(text="Reset", font=(FONT_NAME,20,"bold"),fg="black",bg=YELLOW)
reset_button.config(padx=5,pady=5)
reset_button.grid(column=3,row=4)

count_down(5)
ui.mainloop()