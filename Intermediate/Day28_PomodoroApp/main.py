from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Resets the timer, reps, and title"""
    
    global reps
    reps = 0
    
    window.after_cancel(timer)
    timer_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_label.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """User has pressed the start button and initiated the countdown"""
    
    global reps
    reps += 1
     
    # If rep is currently at final 8th stage
    if reps % 8 == 0:
        timer_label.config(text = "Break", fg = RED)
        countdown(LONG_BREAK_MIN * 60)
        print(reps)

    # If rep is currently at 1/3/5/7 stage
    elif (not reps % 2 == 0):
        timer_label.config(text = "Work", fg = GREEN)
        countdown(WORK_MIN * 60)
        print(reps)
        
    # If rep is currently at 2/4/6 stage
    else:
        timer_label.config(text = "Break", fg = PINK)
        countdown(SHORT_BREAK_MIN * 60)
        print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import math

def format_num(num):
    """Returns a two character version of the number"""
    
    if num < 10:
        num = f"0{num}"
    return num
    
def countdown(count):
    """Takes time in seconds and updates time with the minutes/seconds remaining"""
    
    min_rem = format_num(math.floor(count / 60))
    sec_rem = format_num(count % 60)
    
    canvas.itemconfig(timer_text, text = f"{min_rem}:{sec_rem}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checkmarks = ""
        for _ in range(math.floor(reps / 2)):
            checkmarks += CHECK
        check_label.config(text = checkmarks)


# ---------------------------- UI SETUP ------------------------------- #

# Main window func
window = Tk()
window.title("Pomodoro")
window.geometry('360x380')
window.config(padx = 15, pady = 15, bg = YELLOW)

# Image and countdown timer
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img_file = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img_file)
timer_text = canvas.create_text(105, 130, text = "00:00", fill = "white", font = (FONT_NAME, 30, "bold"))
canvas.grid(column = 1, row = 2)

# Timer Label
timer_label = Label(window, text = "Timer", font = (FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)

# Check Mark Labels
check_label = Label(window, text = "", font = (FONT_NAME, 12, "bold"), fg = GREEN, bg = YELLOW)
check_label.grid(column = 1, row = 4)

# Start Button
start_btn = Button(window, text = "Start", command = start_timer, font = (FONT_NAME, 12, "bold"), bg = "#ffffff")
start_btn.grid(column = 0, row = 3)

# Reset Button
reset_btn = Button(window, text = "Reset", command = reset_timer, font = (FONT_NAME, 12, "bold"), bg = "#ffffff")
reset_btn.grid(column = 2, row = 3)


window.mainloop()