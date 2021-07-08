from utils.ui import UserInterface
from utils.quiz import Question, Quiz
from utils.tools import generate_bool_questions

def main():
    question_bank = []
    questions = generate_bool_questions(10)
    
    for question in questions:
        question_bank.append(Question(question['question'], question['correct_answer']))

    quiz = Quiz(question_bank)
    quiz_ui = UserInterface(quiz)

if __name__ == '__main__':
    main()
