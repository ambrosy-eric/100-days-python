import tkinter
import math

def main():
    ### Disgusting global var maybe fix?
    TIMER = None

    def reset_timer():
        window.after_cancel(TIMER)
        canvas.itemconfig(timer_text, text='00:00')
        title.config(text='Timer')
        checks.config(text='')

    def set_time(reps=0):
        """
        Given a number of reps
        Set the timer text and update labels with either work or breaks
        Odd reps are work, even reps are breaks
        """
        reps += 1
        if reps in [1, 3, 5, 7]:
            update_time(5 * 1, reps)
            title.config(text='Work', fg='#9bdeac')
        elif reps in [2, 4, 6]:
            update_time(5 * 1, reps)
            title.config(text='Break', fg='#e2979c')
        else:
            update_time(20 * 60, reps)
            title.config(text='Break', fg='#e7305b')

    def update_time(time, reps):
        """
        Given a start time
        Update the time, decreasing by 1 second
        """
        mins = math.floor(time / 60)
        if len(str(mins)) < 2:
            mins = f'0{mins}'
        secs = time % 60
        if len(str(secs)) < 2:
            secs = f'0{secs}'

        canvas.itemconfig(timer_text, text=f'{mins}:{secs}')
        if time > 0:
            global timer
            timer = window.after(1000, update_time, time - 1, reps)
        else:
            set_time(reps)
            check_mark = ''
            for _ in range(math.floor((reps+1)/2)):
                check_mark += '✔'
            checks.config(text=check_mark)

    yellow = "#f7f5dd"
    green = "#9bdeac"
    
    window = tkinter.Tk()
    window.title("Pomodoro App")
    window.config(padx=100, pady=50, bg=yellow)

    title = tkinter.Label(text='Timer', fg=green)
    title.config(bg=yellow, highlightthickness=0, font=('Courier', 40, 'bold'))
    title.grid(column=1, row=0)

    canvas = tkinter.Canvas(width=200, height=250, bg=yellow, highlightthickness=0)
    tomato = tkinter.PhotoImage(file='./images/tomato.png')
    canvas.create_image(100, 125, image=tomato)
    timer_text = canvas.create_text(100, 150, text='00:00', fill='white', font=('Courier', 30, 'bold'))
    canvas.grid(column=1, row=1)

    start = tkinter.Button(text='Start', highlightthickness=0, command=set_time)
    start.grid(column=0, row=2)

    reset = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
    reset.grid(column=2, row=2)

    checks = tkinter.Label(fg=green)
    checks.config(bg=yellow, highlightthickness=0)
    checks.grid(column=1, row=3)

    window.mainloop()

if __name__ == '__main__':
    main()
