import tkinter
from utils.quiz import Quiz

class UserInterface():
    """
    Class to create the UI for the Quiz Game
    """

    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        self.theme_color = '#375362'
        self.window = tkinter.Tk()
        self.window.title('Quizzy')
        self.window.config(padx=20, pady=20, bg=self.theme_color)
        self.question = ''
        self.scoreboard = tkinter.Label(text=f'Score: {self.quiz.score}', fg='white', bg=self.theme_color)
        self.scoreboard.grid(column=1, row=0, sticky='EW')
        self.canvas = tkinter.Canvas(width=500, height=450, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(250, 225, width=480, text=self.question, fill=self.theme_color, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, border=0, bg=self.theme_color, activebackground=self.theme_color, command=self.true_answered)
        self.true_button.grid(column=0, row=2, sticky='EW')
        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, border=0, bg=self.theme_color, activebackground=self.theme_color, command=self.false_answered)
        self.false_button.grid(column=1, row=2, sticky='EW')

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """
        Get the next question from the quiz class
        """
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions:
            self.scoreboard.config(text=f'Score: {self.quiz.score}')
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question)
        else:
            self.canvas.itemconfig(self.question_text, text='Quiz Over')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_answered(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_answered(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
