class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        """
        Checks the current question number against the question list
        If that number is greater than the list
        Return False
        """
        if self.question_number < len(self.question_list):
            return True

    def next_question(self):
        """
        Given a question number 
        Retrieve that question from the question list
        Asks user for an answer
        """
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {question.text} (True/False): ')
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Given a user answer and a correct answer
        Determine if they match
        Increase the user score
        """
        if user_answer.lower() == correct_answer.lower():
            print('That is correct')
            self.score += 1
        else:
            print('That answer is incorrect')
        print(f'The correct answer was: {correct_answer}.')
        print(f'Your current score is: {self.score}/{self.question_number}\n')
