import random

def generate_number():
    number = random.randint(1, 100)
    return number

def check_guess(guess, answer):
    """
    Given 2 numbers
    Check if they match
    If not return string 'high' or 'low'
    """
    if guess == answer:
        return True, 'equal'
    elif guess > answer:
        return False, 'high'
    else:
        return False, 'low'
