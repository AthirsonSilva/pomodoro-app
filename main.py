import tkinter

#  CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 5
timer = None

#  TIMER RESET


def reset_timer():
    """
    Timer reset

    Resets the timer looping and the label text
    """

    global timer
    global repetitions
    window.after_cancel(timer)

    # Reseting everything
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_marks.config(text='')
    repetitions = 0


#  TIMER MECHANISM


def start_timer():
    """
    Time starter

    Starts the time according to the repetitions count
    """
    global repetitions

    if repetitions == 5:
        repetitions = 0
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text='Break', fg=RED)

    elif repetitions % 2 == 0:
        repetitions += 1
        count_down(WORK_MIN * 60)
        title_label.config(text='Work', fg=GREEN)

    elif repetitions % 2 == 1:
        repetitions += 1
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break', fg=PINK)

    if repetitions % 2 == 0:
        check_marks.config(text='DONE', font=(FONT_NAME, 20, 'italic'))


#  COUNTDOWN MECHANISM


def count_down(count):
    """
    Counting

    Activates the countdown function

    Arguments:
        count {int} -- The amount to be counted down
    """
    from time import sleep
    import math

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f'0{count_min}'

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        sleep(1)
        global timer
        timer = window.after(100, count_down, count - 1)

    else:
        start_timer()
        mark = ''

        work_session = math.floor(repetitions / 2)
        for i in range(work_session):
            mark += 'DALE'

        check_marks.config(text=mark)


#  UI SETUP
# Window
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = tkinter.PhotoImage(file='projects/pomodoro-start/tomato.png')

# Buttons
start_btn = tkinter.Button(
    text='start', highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=3)

reset_btn = tkinter.Button(
    text='reset', highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=3)

check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Canvas
canvas = tkinter.Canvas(width=200, height=300, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 132, image=tomato_img)
timer_text = canvas.create_text(100, 150, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

title_label = tkinter.Label(text='Timer', fg=GREEN,
                            bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas.grid(column=1, row=2)


window.mainloop()
