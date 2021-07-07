from utils.data import questions
from utils.quiz import Question, Quiz

def main():
    question_bank = []
    for question in questions:
        question_bank.append(Question(question['question'], question['correct_answer']))
    
    quiz = Quiz(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print('Quiz Completed')
    print(f'Your final score was {quiz.score}/{quiz.question_number}')

if __name__ == '__main__':
    main()
