import os
from art import stages, logo
from words import word_list
from utils import chose_word, check_if_completed, is_guessed, update_board, check_guess

def main():
    print(logo)
    lives = 6
    generate_hangman = chose_word(word_list)
    chosen_word = generate_hangman[0]
    board = generate_hangman[1]
    print(" ".join(board))
    guesses = []

    while not check_if_completed(board):
        print(stages[lives])
        guess = input('Please guess a letter\n').lower()
        if is_guessed(guess, guesses):
            print(f'You have already guessed {guess}. Please chose a new letter to guess.')
            guess = input('Please guess a letter\n').lower()
        else:
            guesses.append(guess)
        board = update_board(chosen_word, board, guess)
        print(" ".join(board))
        if not check_guess(chosen_word, guess):
            print(f'{guess.upper()} not found')
            lives -= 1
            print(f'You have {lives} remaining')
        else:
            print(f'{guess} found!')
        if lives == 0:
            print(f'You lose\nThe word was {chosen_word}')
            print(stages[lives])
            return
    print(f'Congratulations you won.\nGuessing {chosen_word} correctly!')
    
if __name__ == '__main__':
    main()