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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text=f'00:00')
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_time_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text='Long Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Timer",fg=GREEN)
        count_down(work_time_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = f'0{minutes}'
    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(int(reps/2)):
            mark += '✔'
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,highlightthickness=10)

timer_label = Label(text="Timer",fg=GREEN, background=YELLOW, font=(FONT_NAME, 30, 'bold'))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 125, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', background=YELLOW, font=(FONT_NAME, 10, 'normal'), width=10, height=2,
                      command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text='Reset', background=YELLOW , font=(FONT_NAME, 10, 'normal'), width=10, height=2, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 10, 'bold'))
check_mark.grid(row=3, column=1)
window.mainloop()
