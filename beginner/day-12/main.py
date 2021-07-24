from utils.art import logo, win_art
from utils.tools import generate_number, check_guess

def main():
    print(logo)
    answer = generate_number()
    print('You will be guess a number between 1 and 100')
    difficulty = input('Please select your difficulty level (easy/hard): ').lower()
    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5
    print(f'You have chosen {difficulty}. You have {lives} guesses available.')
    while lives > 0:
        guess = int(input('Guess a number '))
        check = check_guess(guess, answer)
        if check[0]:
            print(win_art)
            print(f'You won. The number was {answer}')
            return
        elif lives != 1:
            lives -= 1
            print(f'Guess again. Number too {check[1]}.\n{lives} guesses remaining')
        else:
            lives -= 1
    if lives == 0:
        print(f'You have run out of guesses. The correct number was {answer}')

if __name__ == '__main__':
    main()
