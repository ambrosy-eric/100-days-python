import tkinter
from utils.tools import convert_miles

def main():
    window = tkinter.Tk()
    window.title('Miles to Km Converter')
    window.minsize(100, 100)
    window.config(padx=10, pady=10)
    
    miles = tkinter.Entry(width=10)
    miles.grid(column=1, row=0)

    miles_label = tkinter.Label(text='Miles')
    miles_label.grid(column=2, row=0)

    conv_label = tkinter.Label(text='is equal to')
    conv_label.grid(column=0, row=1)

    answer_label = tkinter.Label(text=0)
    answer_label.grid(column=1, row=1)

    km_label = tkinter.Label(text='Km')
    km_label.grid(column=2, row=1)

    def button_clicked():
        answer_label.config(text=convert_miles(miles.get()))

    calc = tkinter.Button(text='Calculate', command=button_clicked)
    calc.grid(column=1, row=2)

    window.mainloop()

if __name__ == '__main__':
    main()
