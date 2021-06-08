import random

def chose_word(word_list):
    """
    Chose a random word
    Generate a list of _ equal to length of the word
    Return it and the random word
    """
    chosen_word = random.choice(word_list)
    word_as_list = []
    for letter in chosen_word:
        word_as_list.append('_')
    return chosen_word, word_as_list
    
def update_board(word, board, guess):
    """
    Given a word, a hangman board and a letter
    Check if the letter is present
    Return True at spot
    """

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            board[position] = letter

    return board

def check_if_completed(board):
    """
    Given a word and a board
    Check if the board is completed
    """
    if '_' in board:
        return False
    else:
        return True

def check_guess(word, letter):
    """
    Given a word and a letter
    Check if the letter is present
    """
    if letter in word:
        return True

def is_guessed(letter, letters_guessed):
    """
    Given a letter and a list of letters
    Check if it has been guessed
    """
    if letter in letters_guessed:
        return True