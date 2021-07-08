import html

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.question = None
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
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.question.text)
        return f'Q.{self.question_number}: {question_text} (True/False): '

    def check_answer(self, user_answer):
        """
        Given a user answer and a correct answer
        Determine if they match
        Increase the user score
        """
        correct_answer = self.question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
