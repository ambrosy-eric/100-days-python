import tkinter
import random
import pandas as pd

current_card = {}
to_learn = {}


def main():
    try:
        data = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pd.read_csv('./data/french_words.csv')
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

    def next_card():
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(to_learn)
        canvas.itemconfig(language, text='French', fill='black')
        canvas.itemconfig(word, text=current_card['French'], fill='black')
        canvas.itemconfig(card_background, image=card_front)

    def flip_card():
        canvas.itemconfig(language, text='English', fill='white')
        canvas.itemconfig(word, text=current_card['English'], fill="white")
        canvas.itemconfig(card_background, image=card_back)

    def is_known():
        to_learn.remove(current_card)
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()


    # Set up UI
    window = tkinter.Tk()
    background_color = '#B1DDC6'
    window.title("French Flash Cards")
    window.config(padx=50, pady=50, bg=background_color)
    flip_timer = window.after(3000, func=flip_card)
    ## Set up button click



    # def button_click():
    #     print(current_card)
    #     source_word = get_word()[0]
    #     print(current_card)
    #     canvas.itemconfig(word, text=source_word)

    # def get_word():
    #     language = list(data_dict.keys())[0]
    #     english = list(data_dict.keys())[1]
    #     ran_int = random.randint(0, len(data_dict[language]) - 1)
    #     word = data_dict[language][ran_int]
    #     eng_translation = data_dict[english][ran_int]
    #     global current_card
    #     current_card.append(word, eng_translation)
    #     return word, eng_translation

    # def flip_card():
    #     canvas.itemconfig(language, 'English')
    #     canvas.itemconfig(word, text=get_word()[1])

    # Set up card
    canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=background_color)
    card_front = tkinter.PhotoImage(file='./images/card_front.png')
    card_back = tkinter.PhotoImage(file='./images/card_back.png')
    card_background = canvas.create_image(400, 263, image=card_front)
    canvas.grid(column=0, row=0, columnspan=2)

    language = canvas.create_text(400, 150, font=('Ariel', 34, 'italic'), text='')
    word = canvas.create_text(400, 263, font=('Ariel', 48, 'bold'), text='')

    # Set up buttons
    right_image = tkinter.PhotoImage(file="./images/right.png")
    right_button = tkinter.Button(image=right_image, border=0, bg=background_color, activebackground=background_color, command=is_known)
    right_button.grid(column=1, row=1, sticky='EW')

    wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
    wrong_button = tkinter.Button(image=wrong_image, border=0, bg=background_color, activebackground=background_color, command=next_card)
    wrong_button.grid(column=0, row=1, sticky='EW')
    
    window.mainloop()

if __name__ == '__main__':
    main()
